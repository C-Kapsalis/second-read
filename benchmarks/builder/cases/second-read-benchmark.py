"""Planted-flaw benchmark for Second Read's copy skill.

Cases: the ten emails of email-benchmark.md as sr-email-01..10, plus the
seven social posts, seven landing pages and seven blog drafts of
second-read-benchmark.md (six flawed and one clean control per format).
Graded on flaw recall, gate flaws first, decoys left alone, no invented facts
in the rewrite, and the control's verdict."""

import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
from common import write_case  # noqa: E402

SKILL = r'"skill"\s*:\s*"(second-read:)?second-read"'

# Facts in each benchmark email (and its context line) that a rewrite may use.
EMAIL_FACTS = {
    1: "From Larkspur & Vine, hello@larkspurandvine.com; recipient Jordan; biggest sale of the season; 40% off everything sitewide; free shipping on every order; Linen Wrap Dress $77.40 (was $129); Everyday Wide-Leg Trouser $53.40 (was $89); Woven Market Tote $35.40 (was $59); signed up at larkspurandvine.com; unsubscribe and privacy policy links; (c) 2026 Larkspur & Vine.",
    2: "From Dana Whitfield, Head of Finance Ops at Tallyhawk, dana@tallyhawk.io; webinar Thursday 12 November at 4 PM (no time zone given); two controllers from mid-size companies; close cut from 10 days to 3, 70%; automated reconciliations; their checklist and a template; 2026 Close Benchmark ebook; 1:1 demo; LinkedIn; Tallyhawk Inc., 410 Harbor Street, Suite 900, Boston, MA 02110; unsubscribe and manage preferences links; sent Tuesday 10:00 local.",
    3: "From Ember Grind, orders@embergrind.com; recipient Chris; cart items (from the context): Ember Burr Grinder Pro and 2 x Single-Origin Ethiopia 250g; founded 2014 in a garage in Leeds by Tom and Aisha; roast six days a week in small batches; roast date on every bag; beans from Ethiopia, Colombia, Guatemala and Rwanda; two years testing burr shapes; compostable bags, recycled boxes, carbon offset via a reforestation partner in Uganda, impact report every spring; code EMBER10 for 10% off, valid until Sunday 23:59 CET; link https://bit.ly/3xEmbr; Ember Grind Ltd, Unit 4, Canal Works, Leeds LS1 4BR, United Kingdom; unsubscribe and privacy links.",
    4: "Previously sent as Coach Mia at Stridewell (context); Stridewell Running Club, 22 Fenwick Road, Bristol BS3 1QF; signed Mia; Spring Half Marathon, registration closes Friday (inside the image); hill repeats: 60 to 90 seconds, six to eight reps, once a week for six weeks; Riverside Loop flat 8 km with a water fountain at the halfway bridge; Quarry Hill Out-and-Back 12 km with 180 m of climbing; Old Railway Path traffic-free 15 km; race-day checklist: breakfast three hours before, arrive 45 minutes early, ten-minute warm-up; Sunday's club run; unsubscribe and update preferences links.",
    5: "From Fork & Field, hi@forkandfield.com; recipient Sam; inactive 4 months; 14 boxes together; autumn menu with 22 new recipes; miso squash bowl Sam rated five stars in March; 'a special discount' with no amount; account deletion in 24 hours (claim); Fork & Field, 88 Mercer Lane, Portland, OR 97209.",
    6: "From Priya at Lumen Botanics, priya@lumenbotanics.com; recipient Alex; the sign-up form promised 15% off the first order (context); Dawn Renewal Serum; claims 'clinically proven #1 serum in the world' and 'cure your acne in just 7 days' (unsupported); founder's 3-step routine: Cloud Gel Wash morning and night, two drops of Dawn Renewal Serum on damp skin, Daily Barrier Cream; Lumen Botanics, 15 Orchard Row, Asheville, NC 28801; unsubscribe and privacy links.",
    7: "From Quarry, news@quarrydata.com; recipient Morgan; Quarry 3.0; CDC ingestion, columnar OLAP layer, incremental materialisation, ELT pipeline; dashboards no longer depend on nightly batch jobs that fail silently; new pricing tiers (no prices given); contact the sales team; Quarry Data Inc., 77 Mission Street, San Francisco, CA 94105; unsubscribe and manage preferences links; scheduled Saturday 02:00.",
    8: "From Ines at Paper Lantern Books, ines@paperlanternbooks.com; Ilse Marren; new novel The Salt Orchard; Ines missed her bus stop twice in one week; Thursday, 14 November 2026 at 7 PM (weekday wrong: it is a Saturday); 'our new location' (no address); reading, conversation and signing; wine and cake; Paper Lantern account and 9-question RSVP form; seats limited to 60; Ines, owner; Paper Lantern Books, 3 Wren Street, Galway H91 E2K4, Ireland; unsubscribe link.",
    9: "From Coinpath Security Team, security@coinpath.app; recipient Taylor; $100 cash for every friend who joins with your link; link http://coinpath.app/refer/taylor; offer ends 31 October 2026 because the partner bank's promotion ends; condition: friend deposits at least $500 and keeps it 90 days; attachment Referral_Terms.pdf; Coinpath is a financial technology company, not a bank; Harbour Mutual Bank, Member FDIC; crypto assets not FDIC insured and may lose value; Coinpath Inc., 500 Pine Street, Seattle, WA 98101; unsubscribe and privacy links.",
    10: "From Hana at Kiln & Clay Studio, hana@kilnandclay.com; recipient Robin; six new glazes; Ember Rust, Fog Celadon, Tidepool Blue; mixed by hand, fired in batches of about 40 pieces; sold-out colours return in spring; members get first pick until Friday 23 October, 23:59 GMT; mugs from £28, serving bowls from £64; ships in 2 working days; returns within 30 days; quote from Elena R., member since 2022; Kiln & Clay Studio, 12 Potters Yard, Bath BA1 2QH, United Kingdom; manage preferences or unsubscribe.",
}

EMAIL_PROMPTS = [
    "Can you give this email a second read before it goes out? Context: {context}",
    "We're about to schedule this one. Could you give it a second read and tell me what to fix? Context: {context}",
    "Second pair of eyes please: is this email ready to send? Context: {context}",
]

KIND = {"social": "post", "landing": "page", "blog": "article", "email": "email"}


def graders_for(kind, flaws, decoys, facts, original):
    """flaws: [(id, description, is_gate)]. Empty flaws means a clean control."""
    noun = KIND[kind]
    out = []
    if flaws:
        need = max(1, int(0.8 * len(flaws) + 0.5))  # 80%, rounded to the nearest flaw
        listing = "\n".join(f"- {fid}: {desc}" for fid, desc, _ in flaws)
        out.append(("flaw-recall", 3, f"""
The {noun} has {len(flaws)} planted problems:
{listing}

A problem counts as found when report.md identifies the same problem with evidence (a quote, a count, or the specific element), in the fix list or the list of failed checks. Wording need not match. Vague remarks ("the hook could be stronger") do not count, and "not visible, please confirm" counts as not found when the element is in the {noun}.

PASS if at least {need} of the {len(flaws)} problems are found.
FAIL otherwise.
"""))
        gates = [f"{fid}: {desc}" for fid, desc, g in flaws if g]
        if gates:
            out.append(("gate-flaws-first", 2, f"""
These problems are severe enough that the {noun} should not go out until they are fixed:
{chr(10).join('- ' + g for g in gates)}

PASS if report.md gives a "do not send" verdict (or "do not post", "do not publish", "not ready", "fix before sending/posting/publishing") AND each listed problem appears among its top-ranked fixes (the first five fixes).
FAIL if the verdict says it is ready to go, or any listed problem is missing from the top fixes.
"""))
        if decoys:
            out.append(("decoys-left-alone", 1, f"""
These aspects of the {noun} are correct and must NOT be reported as problems: {decoys}
Asking for a source, a date or a link for one of them is fine and does not count as flagging it; only presenting it as an error or a mistake to remove does.

PASS if report.md does not flag any of these as a problem in its fix list or failed checks (mentioning them neutrally or as a strength is fine).
FAIL if any of them is presented as an error or a fix to make.
"""))
    else:
        out.append(("control-verdict", 3, f"""
This {noun} is a well-built control with no planted problems.

PASS if report.md's verdict is positive (ready to send, ready to post or publish, or minor polish only), it does NOT say "do not send" or "fix first" / "not ready", and it does not present any serious problem (no blocker or major issue for a real defect).
FAIL if it says the {noun} should not go out as is, or invents a serious problem.
"""))
    out.append(("no-invented-facts", 2, f"""
The facts in the original {noun} (and its brief) are:
{facts}

The original, for reference:
<original>
{original.strip()}
</original>

Check the rewritten version in report.md (and any rewritten lines or alternative headlines, subjects or captions it offers).

PASS if the rewrite adds no price, discount, percentage, count, date, weekday, time, deadline, time zone, statistic, rating, review, testimonial, quote, name, address, link, guarantee, award or product claim that is not in the facts above. Bracketed placeholders such as [end date], [source] or [confirm: 14 or 30 days] are fine, so is a question to the marketer, and so is removing a fact. Restating a fact in other words is fine; a new number is not, even if it is arithmetically correct (for example a computed saving). If report.md gives no rewrite because the piece is ready, PASS.
FAIL if the rewrite contains any such new fact.
"""))
    return out


def build(name, kind, filename, content, prompt, graders):
    write_case(
        name,
        {f"resources/{filename}": content.rstrip("\n") + "\n"},
        f"resources/{filename} is the {KIND[kind]}. {prompt}\n\nIf it needs changes, send me a fixed version too, as one fenced code block I can paste.",
        graders,
        skill_match=SKILL,
    )


# Emails: reuse email-benchmark.md.
text = (HERE / "email-benchmark.md").read_text()
sections = re.split(r"^## Email (\d+): (.+)$", text, flags=re.M)
for i in range(1, len(sections), 3):
    num, title, body = int(sections[i]), sections[i + 1].strip(), sections[i + 2]
    context = re.search(r"Context: (.+?)\n\n", body, re.S).group(1).replace("\n", " ").strip()
    email = re.search(r"```\n(.*?)\n```", body, re.S).group(1)
    flaws = [
        (m.group(1), m.group(3).strip(), bool(m.group(2)))
        for m in re.finditer(r"^\| (\d+\.\d+)( \*\*gate\*\*)? \| (.+?) \|.*$", body, re.M)
    ]
    decoys = re.search(r"Decoys?:(.+?)(?:\n\n|\Z)", body, re.S)
    decoys = decoys.group(1).replace("\n", " ").strip() if decoys else ""
    prompt = EMAIL_PROMPTS[num % 3].format(context=context)
    name = f"sr-email-{num:02d}"
    build(name, "email", "email.txt", email, prompt,
          graders_for("email", flaws, decoys, EMAIL_FACTS[num], email))
    print(f"{name}: {title}; {len(flaws)} flaws, {sum(g for *_, g in flaws)} gate")

# Social posts, landing pages, blogs: second-read-benchmark.md.
text = (HERE / "second-read-benchmark.md").read_text()
sections = re.split(r"^## (sr-(social|landing|blog)-\d+): (.+)$", text, flags=re.M)
for i in range(1, len(sections), 4):
    name, kind, title, body = sections[i], sections[i + 1], sections[i + 2].strip(), sections[i + 3]
    field = lambda key: re.search(rf"^{key}: (.+)$", body, re.M).group(1).strip()  # noqa: E731
    content = re.search(r"```\w*\n(.*?)\n```", body, re.S).group(1)
    flaws = [
        (m.group(1), m.group(3).strip(), bool(m.group(2)))
        for m in re.finditer(r"^\| ([A-Z]?\d+\.\d+)( \*\*gate\*\*)? \| (.+?) \|.*$", body, re.M)
    ]
    decoys = re.search(r"^Decoys: (.+)$", body, re.M)
    decoys = decoys.group(1).strip() if decoys else ""
    is_control = "Control: no planted flaws" in body
    assert is_control == (not flaws), name
    assert is_control or (3 <= len(flaws) <= 6 and decoys), name
    prompt = f"{field('Prompt')}\n\nContext: {field('Context')}"
    build(name, kind, field("File"), content, prompt,
          graders_for(kind, flaws, decoys, field("Facts"), content))
    print(f"{name}: {title}; {len(flaws)} flaws, {sum(g for *_, g in flaws)} gate")
