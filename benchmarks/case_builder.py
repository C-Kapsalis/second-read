#!/usr/bin/env python3
"""Developer-only generator of the committed, synthetic paired editorial fixtures."""
import json
from pathlib import Path
cases = [
('scope-all','policy','edit','Our pilot surveyed eight riders. All commuters prefer this route.','All commuters prefer this route.','Draft moves from eight riders to everyone; qualify the target group.','The pilot surveyed eight riders; its results alone cannot establish what all commuters prefer.'),
('scope-bounded','policy','leave','Among eight riders interviewed, six preferred this route.','six preferred this route.','Bounded sample claim is appropriately scoped; do not universalize.',None),
('modal-strengthen','docs','edit','We are considering offline export. Offline export is now available.','Offline export is now available.','Proposed feature incorrectly becomes shipped.','Offline export is under consideration.'),
('modal-caution','docs','leave','Offline export may become available after testing.','may become available','Appropriately conditional product statement stays.',None),
('causal-leap','journalism','edit','Areas with more buses had higher attendance. More buses caused attendance to rise.','More buses caused attendance to rise.','Association is not causal proof.','Areas with more buses also recorded higher attendance; this comparison alone does not establish causation.'),
('causal-careful','journalism','leave','Attendance rose in the same period, though this does not show the buses caused it.','this does not show the buses caused it.','Already preserves epistemic limitation.',None),
('metaphor-strong','essay','leave','A timetable is a promise. When the bus does not come, the city breaks it.','A timetable is a promise.','Memorable ethical metaphor is not statistical reporting.',None),
('metaphor-evidence-misused','essay','edit','Imagine a nurse waiting at midnight. This proves every night worker faces a long wait.','This proves every night worker faces a long wait.','Hypothetical example cannot establish prevalence.','The example shows why a long wait can matter; it does not establish how often it happens.'),
('imagined-nurse','essay','leave','Imagine a nurse finishing a late shift and waiting for a bus.','Imagine a nurse finishing a late shift','Imagine already marks the scenario as hypothetical; no disclaimer.',None),
('generic-ai-opening','blog','edit','In today’s fast-paced world, it is important to leverage seamless innovation. Our guide covers the setup command.','In today’s fast-paced world, it is important to leverage seamless innovation.','Empty generic opening obscures real task.','This guide explains the setup command.'),
('brand-slogan','brand','leave','Read it twice. Send it once.','Read it twice. Send it once.','Specific, memorable parallelism; not generic just because symmetrical.',None),
('intentionally-fragment','fiction','leave','Not this time.','Not this time.','A meaningful fragment is not a grammar error.',None),
('narrative-knowledge','fiction','ask','Nina had never read the letter. In the next room, she quoted its last line.','she quoted its last line.','Unexplained knowledge may be a deliberate reveal; author intent decides.','Did Nina learn the line off-page or is this deliberate dramatic irony?'),
('fiction-subtext','fiction','leave','She put the key on the table. Neither reached for it.','Neither reached for it.','Preserve emotional ambiguity; do not explain inferred motives.',None),
('essay-orphan','essay','edit','The article lists three emails promising different launch dates. Then it abruptly turns to typography.','Then it abruptly turns to typography.','Reader may not know what conflicting emails illustrate.','These inconsistent dates leave subscribers uncertain about when the product launches.'),
('policy-ambiguous','policy','ask','We should test the bus route for six months. That is why fares must be abolished immediately.','fares must be abolished immediately.','Two incompatible policy positions; do not choose without brief.','Is the policy to test reliability first or remove fares now?'),
('docs-prereq-late','docs','edit','Run the setup command with $TOKEN. In the last section we explain how to obtain a token.','Run the setup command with $TOKEN.','Credential prerequisite occurs too late; move supplied instruction or link earlier.','First obtain a token using the documented procedure, then run the setup command with $TOKEN.'),
('docs-reference-clean','docs','leave','API reference: `timeout` (integer, default 30).','`timeout` (integer, default 30).','Reference data can be concise; do not force a tutorial.',None),
('canonical-us-spelling','docs','edit','Project house style is the Canonical Documentation Style Guide. To initialise the service, open the terminal.','To initialise the service, open the terminal.','Canonical currently uses US spelling when this project adopts it.','To initialize the service, open the terminal.'),
('canonical-outside-scope','docs','leave','Our project uses British English, not Canonical house style. To initialise the service, open the terminal.','To initialise the service, open the terminal.','Do not apply Canonical spelling outside its chosen project.',None),
('email-subject-mismatch','email','edit','Subject: Your account is active. Body: Join the waitlist for an invitation.','Your account is active.','Subject promises access not offered in body.','Join the waitlist for an invitation.'),
('personal-email','email','leave','I read your interview about late shifts. Your final answer stayed with me.','Your final answer stayed with me.','Personal specificity should not become marketing filler.',None),
('campaign-rule','brand','edit','Project brief: This is a seven-day trial. Email: Try the full product free forever.','Try the full product free forever.','Explicit project offer conflicts with draft.','Try the product free for seven days.'),
('brief-absent','brand','ask','The offer is available now, but the briefing supplies no plan, price or availability evidence.','The offer is available now','Cannot validate promise without brief/source; ask rather than invent.','Is the offer actually live and to which readers does it apply?'),
('seo-stuffed-title','blog','edit','Article covers one missing setup prerequisite. Title: The Ultimate Complete Guide to Every Installation Problem.','The Ultimate Complete Guide to Every Installation Problem.','Title overpromises content and search intent.','Fix a missing prerequisite during setup.'),
('seo-clear-direct','blog','leave','How do I reset the token? Follow these tested steps.','How do I reset the token?','Question is accurately framed and answered directly.',None),
('landing-cta-wrong','landing_page','edit','The approved next step is an online sandbox. Button: Book a sales demo.','Book a sales demo.','CTA mismatches actual destination.','Open the sandbox.'),
('landing-paths','landing_page','leave','Documentation home: Start a tutorial / Browse API reference.','Start a tutorial / Browse API reference.','Two actions serve different legitimate user jobs.',None),
('ad-absolute','ad','edit','Product backs up once daily. Ad: Never lose a file again.','Never lose a file again.','Unbounded absolute promise unsupported by daily backup.','Back up your files automatically each day.'),
('ad-short-joke','ad','leave','Customer: How many retweets? Brand: 18 million.','18 million.','Brevity acquires meaning from the supplied conversational context.',None),
('ads-disclosure','ad','ask','The post promotes a paid partner product, but no relationship disclosure is visible.','promotes a paid partner product','Disclosure requirements depend on audience and jurisdiction, and exact sponsor relationship.','Where will the ad appear and what is the material relationship?'),
('oxford-house-style','journalism','ask','University newsroom piece. It may follow Oxford University Style Guide or a separate publication house guide.','may follow Oxford University Style Guide','Oxford university style is not universal reporting policy; which house guide applies?','Which style guide has been approved for this publication?'),
('journalistic-attribution','journalism','edit','The department projects £20 million in savings. Experts agree it will save £20 million.','Experts agree it will save £20 million.','One departmental forecast cannot establish expert consensus.','The department forecasts £20 million in savings.'),
('reported-attribution-clean','journalism','leave','In its unverified forecast, the department estimated £20 million in savings.','In its unverified forecast','Clear provenance and uncertainty; do not imply consensus.',None),
('chart-long-series','journalism','visual','The story lists 12 yearly observations for eight regions and asks readers to compare trends.','12 yearly observations for eight regions','A chart may make multiseries temporal comparison easier if underlying data are comparable.','Visual suggestion: small-multiple line charts with year, unit, source and accessible text.'),
('chart-two-numbers','journalism','leave','Applications rose from 10 to 12 in the supplied annual figures.','rose from 10 to 12','A one-sentence comparison is clearer than a decorative chart.',None),
('seo-no-word-count','blog','leave','We answered the reader’s question in 350 clear words.','in 350 clear words.','Google does not prescribe a magic word count; leave good concise answer.',None),
('multilingual-idiom','essay','leave','The results were inconclusive.','The results were inconclusive.','Standard English is not suspicious and does not need slang to sound human.',None),
('bridge-redundant','essay','leave','She waited for the bus. It never came.','It never came.','Consequence is clear; forced connective adds noise.',None),
('product-unverified','docs','ask','The draft claims “The CLI syncs accounts automatically” but no product version or runtime evidence was provided.','The CLI syncs accounts automatically','Cannot verify live behavior from prose alone.','Which product version and authorized source/runtime evidence supports automatic sync?'),
('strong-cta','landing_page','leave','Approved page opens plan comparisons. Button: Compare plans.','Compare plans.','CTA accurately describes action and is specific.',None),
]

out=[]
for id,pathway,decision,draft,quote,reason,content in cases:
 obj={'id':id,'pathway':pathway,'decision':decision,'draft':draft,'source_quote':quote,'reason':reason}
 if decision=='edit': obj['safe_edit']=content
 elif decision=='ask': obj['question']=content
 elif decision=='visual': obj['visual_reason']=content
 out.append(obj)
root=Path(__file__).parent
(root/'editorial_cases.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in out)+'\n',encoding='utf-8')
print(len(out))
