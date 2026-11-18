# VNUK Digital Transformation Project Context

Updated: 11 November 2026

## Project direction

- Long-term product: VNUK Student Support and Academic Navigation.
- MVP model: journey-led product pod.
- MVP journey: academic enquiry support and routing.
- Core journey: student asks a question -> the system identifies the topic -> approved guidance is retrieved -> the student receives next steps -> unresolved cases are routed to the relevant department -> staff and student confirm status and usefulness.
- The MVP uses one authenticated student-facing front door. Existing systems and departmental ownership remain behind it.

## MVP test scenarios

The MVP should test one journey through three representative scenarios:

1. Course-registration questions.
2. Academic-advising questions.
3. Graduation or project-milestone questions.

These are scenarios within one journey, not three separate products.

## Out of scope

- Automatically registering courses.
- Changing EMS, LMS or official academic records.
- Accessing grades, tuition status or live enrolment records.
- Making academic eligibility, financial or graduation decisions.
- Replacing institutional email or the university's full ticketing system.
- University-wide rollout during the MVP.
- Automatic model retraining from student conversations.

Read-only identity verification is in scope. The portal should verify approved student or staff accounts through the institutional identity directory without reading or changing academic records.

## Team roles

| Person or role | Responsibility |
|---|---|
| Maddie | Business Analyst and Product Owner. Handles client-facing requirements, Product Goal, backlog, acceptance criteria, process mapping and performance questions. |
| Tamas | Software Engineer and Technical Lead. Owns the portal, server, AI/API and email-service integration. |
| Zsombi | Software Engineer and Data and Integration Lead. Owns identity verification, database, retrieval, event logging and monitoring. |
| Yuhan | UX/UI, User Research and QA Lead. Owns the student journey, usability testing, test cases, feedback and product improvements. |
| Academic Affairs content owner | Approves authoritative academic guidance and updates it when policies change. Named institutional owner still needs confirmation. |
| VNUK IT/privacy adviser | Reviews identity, security, retention, hosting and AI-risk controls. Named reviewer still needs confirmation. |

Research is shared between the BA and UX/UI roles. A separate full-time researcher, project manager or data scientist is not required for this small MVP.

## Interfaces and architecture

### User-facing interfaces

- Authenticated student portal or chat/intake interface.
- Staff email containing the request ID and full context.
- Staff status-update and closure link.
- Student and staff feedback/rating view.
- Approved-content administration view.

### System interfaces

- Read-only institutional identity directory or SSO.
- Approved knowledge repository.
- Retrieval mechanism or vector search.
- Optional AI service/API.
- Institutional email service.
- Request and status store.
- Analytics and audit event log.
- Monitoring webhook or team alert.

The centralized front door centralizes access and routing; it does not replace EMS, LMS, official academic systems or departmental ownership.

## Request workflow

1. Student signs in through a verified account.
2. Student selects or describes an academic enquiry.
3. The system retrieves approved guidance with source, owner and review date.
4. If the answer is sufficient, the student can rate it from 1 to 5 and explain a low rating.
5. If the evidence is insufficient, the system refuses to invent an answer.
6. The system shows the relevant department and pre-fills an email with the question, context and request ID.
7. The department receives the email and the student can receive a copy.
8. Staff update status or closure through an embedded link.
9. The system records routing, response, resolution, feedback and duplicate-routing events.
10. Unanswered or poorly rated cases enter a reviewed content-gap queue.

## Safety and fallback

- Uncertain or unsupported questions must escalate instead of receiving a guessed answer.
- If the portal is unavailable, show a static status page and direct department email directory.
- Send a monitoring webhook to the team for outages, repeated failures or email-delivery problems.
- If email delivery fails, retain the request and show a retry/reference status.
- Use one request ID to prevent duplicate routing.
- Send a reminder for unresolved requests after the agreed response window.
- Urgent requests should have a visible direct-department route.

## Content and AI governance

- Academic Affairs approves and maintains authoritative guidance.
- Guidance items require a source, owner, applicable context and review date.
- Poorly rated or unanswered interactions are reviewed as content gaps.
- Maddie and the Academic Affairs content owner classify the gap, approve any content change and refresh the retrieval index.
- Student conversations are not automatically used to retrain the model.
- AI may classify enquiries, retrieve approved content, summarize long messages and draft staff responses.
- AI must not infer registration status, eligibility, grades, tuition liability or other official decisions.

## Pilot

- Participants: five students, supported by staff from the same service journey.
- Duration: three weeks.
- Method: short Agile cycles of test, feedback, backlog update, fix or refinement and retest.
- The pilot is a usability and workflow test, not evidence of university-wide prevalence or impact.

## Proposed pilot thresholds

These are proposed thresholds, not measured VNUK baselines:

- At least 80% of assessed answers receive a usefulness rating of 4 or 5 out of 5.
- Zero critical wrong guidance involving eligibility, grades, finance or official records.
- At least 80% of assessed handoffs reach the correct owner on first assignment.
- No material increase in total staff effort per resolved case after maintenance and escalation effort are included.
- No unresolved duplicate routing.
- 100% of published guidance has an approved source, owner and review date.
- Compare repeat contact and resolution time with the baseline once the pilot baseline is captured.

## Pause criteria

Pause the AI/retrieval layer when:

- unsupported or incorrect answers occur repeatedly;
- routing accuracy is poor;
- staff workload increases materially;
- duplicate cases or unresolved handoffs occur;
- identity, privacy or access controls fail;
- content has no accountable owner; or
- the system cannot show source or review information.

The non-AI guidance, intake and email-routing workflow may continue if it remains safe and useful.

## Stop criteria

Stop the MVP when:

- students do not use it after onboarding and usability fixes;
- the team cannot maintain the approved knowledge base;
- no VNUK department accepts ownership;
- approved access or privacy controls cannot be established;
- critical errors remain unresolved; or
- the pilot shows no credible improvement after corrective iterations.

## Backlog

The report contains an ordered backlog. The separate backlog documents are raw or simulated discovery artefacts, not the final committed backlog.

The final backlog should include:

- ID and user story;
- priority;
- owner;
- acceptance criteria;
- dependency;
- status;
- effort estimate;
- evidence source; and
- definition of done.

Initial MVP backlog:

1. Authenticated access.
2. Approved content structure.
3. Request-category selection.
4. Guided student intake.
5. Retrieval from approved guidance.
6. Safe uncertainty fallback.
7. Correct department routing.
8. Email with request ID and context.
9. Staff status and closure link.
10. Student and staff feedback.
11. Analytics and audit logging.
12. Monitoring and outage notification.

## RACI direction

The RACI should be task-level with exactly one accountable owner per row. The revised report uses these task groups:

- define requirements, journey scope and ordered backlog;
- map and test the student enquiry journey;
- approve academic guidance and review policy changes;
- build the portal, routing, AI and email workflow;
- implement identity, logging, retention and monitoring controls;
- run usability, QA and pilot feedback cycles; and
- decide continue, pivot, pause or stop.

## Session 9 presentation story

The presentation should connect:

1. The change impact on students, staff resolvers, content owners and IT/privacy.
2. The named roles and task-level RACI.
3. The three-week adoption and pilot roadmap.
4. The unit of scale: a programme or repeatable academic-enquiry category.
5. The reusable core: portal pattern, knowledge schema, taxonomy, routing, request ID, email handoff, metrics, privacy controls and governance.
6. Local configuration: contacts, policies, programme/cohort rules and review calendars.
7. KPIs, thresholds, feedback, pause criteria and stop criteria.
8. A prototype walkthrough showing the student question, retrieved answer, email handoff, request ID, staff status link and feedback loop.

## Current revised deliverable

- Revised report: `DBB43005_Group1_VNUK_Report_REVISED.docx`
- Original report retained unchanged: `DBB43005_Group1_VNUK_Report.docx`
- The revised report was rendered and visually checked after editing.

## Remaining confirmations before final submission

- Confirm the actual name of the Academic Affairs content owner.
- Confirm the actual VNUK IT/privacy reviewer.
- Confirm the response-time or SLA target for staff handoff.
- Confirm whether the five pilot students represent one programme or multiple programmes.
- Confirm the final technical stack and hosting choice.
- Confirm whether the Session 9 presentation should be a concise 15-minute executive deck or a detailed workshop-style deck.
