from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "/Users/lyndalevy/Desktop/Week2_StudyGuide.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=0.45*inch,
    rightMargin=0.45*inch,
    topMargin=0.35*inch,
    bottomMargin=0.35*inch,
)

styles = getSampleStyleSheet()

NAVY  = colors.HexColor("#1a2e5a")
TEAL  = colors.HexColor("#1e6b72")
LGRAY = colors.HexColor("#f0f4f8")
MGRAY = colors.HexColor("#c8d4e0")

title_style = ParagraphStyle(
    "Title2", parent=styles["Normal"],
    fontSize=13, leading=16, textColor=NAVY,
    fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=2,
)
sub_style = ParagraphStyle(
    "Sub", parent=styles["Normal"],
    fontSize=7.5, leading=9.5, textColor=colors.HexColor("#4a4a4a"),
    fontName="Helvetica", alignment=TA_CENTER, spaceAfter=4,
)
lec_header_style = ParagraphStyle(
    "LecH", parent=styles["Normal"],
    fontSize=8.5, leading=11, textColor=colors.white,
    fontName="Helvetica-Bold", alignment=TA_LEFT,
)
slide_style = ParagraphStyle(
    "Slide", parent=styles["Normal"],
    fontSize=7, leading=9.2, textColor=colors.HexColor("#1a1a1a"),
    fontName="Helvetica", spaceBefore=2, spaceAfter=0,
)
note_style = ParagraphStyle(
    "Note", parent=styles["Normal"],
    fontSize=6.3, leading=8, textColor=colors.HexColor("#555555"),
    fontName="Helvetica-Oblique", leftIndent=6, spaceBefore=0, spaceAfter=1,
)

def b(text): return f"<b>{text}</b>"
def i(text): return f"<i>{text}</i>"

LECTURE_1 = [
    ("1.1", "Setup Checkpoint",
     "Run <font name='Courier' size='6.5'>claude --version</font>; sort into categories A–D "
     "(ready / error / no access / not started).",
     None),
    ("1.2", "Course Site Navigation",
     "Click three course links; find a real 404 on the Announcements page. "
     "Distinguish observable symptoms from unknown causes.",
     "The 404 is genuine — see it live on the projector before anything is described."),
    ("1.3", "Unverified Response",
     "Asking AI without the URL → unverified guess. "
     "<i>\"Nothing was checked. It never opened the page. Status: unverified.\"</i>",
     "Do not require a device; the unverified answers students return are all the point."),
    ("1.4", "Agent Capability",
     "<b>Definition:</b> <i>\"A model that can look, whose next move depends on what it saw, "
     "and that can decide to look again, is an agent.\"</i> Four moves: read → ask permission → look → propose then stop.",
     "Hold step 1 until most pairs have three verbs down."),
    ("1.5", "Text Message Exercise",
     "Questions answerable from memory vs. questions requiring real-world observation — "
     "tool access enables the instinct to \"look it up.\"",
     None),
    ("1.6", "Write Instructions Once",
     "In pairs, write a 3–5 step broken-link procedure. "
     "<b>Skill</b> = reusable procedure; <b>Tool</b> = one action returning one result.",
     "Hold step 1 for the full three minutes even if the room goes quiet."),
    ("1.7", "One Look Only",
     "Three sequential observations each depend on the previous — cannot be planned in advance; a loop is required.",
     None),
    ("1.8", "Write a Loop",
     "Formulate the rule: what to examine, what to do with each answer, when to stop (termination condition).",
     "Real loop demo — ccunpacked.dev, \"The Agent Loop\" at 0.5×; step 7 = decide, step 8 = repeat, step 11 = stop."),
    ("1.9", "Role-Play Simulation",
     "Four roles: Goal Keeper, Model, Host/Tool, Reviewer/Recorder — reveals where human authority boundaries must sit.",
     None),
    ("1.10", "Ambiguous Instruction",
     "\"Fix the Announcements link\" permits three violations: editing without permission, guessing without evidence, "
     "no stop rule. Introduces the <b>Agent Brief</b>: Outcome · Evidence · Limits · Stop Rule.",
     None),
    ("1.11", "Study Guide Lab",
     "Write a four-part brief; run against an approved source; verify two claims; request one change. <i>15-min lab.</i>",
     "Use the linked worksheet — four-part builder, live/supplied-context/simulated routes, print-preview check."),
    ("1.12", "Accept the Report?",
     "Agent claims: <i>\"Fixed the Announcements link and verified it works.\"</i> "
     "Most accept — the acceptance is the lesson.",
     "Take a show of hands before revealing; record the split."),
    ("1.13", "Trace Reveals Problems",
     "Six entries in record. <b>Entry 5</b>: edited without permission. "
     "<b>Entry 6</b>: claimed verification without evidence. "
     "<i>\"The report hid both; the record cannot.\"</i>",
     "Let them hunt two full minutes before revealing."),
    ("1.14", "Write Permissions",
     "Draft a permission making Entry 5 legal: (a) narrow permission + verification, "
     "or (b) keep read-only with human application.",
     "Test each permission aloud — what may it change, what must it show, where does it stop?"),
    ("1.15", "Three More Failures",
     "Study-guide agent: read unauthorized notes · invented unsupported deadline · emailed draft without permission. "
     "Each gap needs its own boundary.",
     "Run all three as a quick show of hands before revealing."),
    ("1.16", "Four Safeguard Layers",
     "Build boundaries across: (1) Context/Privacy, (2) Tools/Permissions, "
     "(3) Evidence/Checks, (4) Stop/Hand-off.",
     "Require enforceable controls — \"be safe\" is not a control."),
    ("1.17", "Exit Ticket",
     "(1) LLM fluency ≠ verification. (2) Agents use skills + tools by looping. "
     "(3) Systems must stop and hand off at consequential action points.",
     "Collect two contrasting boundary examples aloud; preview Meeting 2."),
]

LECTURE_2 = [
    ("2.1", "Where Is Your Study Guide?",
     "Three locations: chat, saved file, agent memory. Reveal: <b><i>\"Save a file you can reopen.\"</i></b>",
     None),
    ("2.2", "Save, Commit, or Push?",
     "Four locations (file, folder, history, GitHub) → three moves. "
     "Only <b>push</b> leaves the computer; save and commit stay local.",
     "Point at each of the four places as you read them, then again during demo."),
    ("2.3", "Git vs. GitHub",
     "<b>Git</b> = local software for checkpoints/version recovery. "
     "<b>GitHub</b> = website for reaching other computers. Neither requires the other.",
     "Three minutes, immediately before the setup window."),
    ("2.4", "Workshop Doorway",
     "External workshop for hands-on Git setup and a shared save/commit/push demonstration.",
     None),
    ("2.5", "Approve the Destination",
     "Before pushing: verify the exact destination AND contents in the browser — "
     "a \"success message\" is a claim; opening GitHub is evidence.",
     "Private repository — pushing does not publish a website; read actual errors aloud."),
    ("2.6", "Improve One Sentence",
     "Fix one sentence → create a <b>diff</b> (side-by-side before/after). "
     "Second checkpoint records the change; update <font name='Courier' size='6.5'>next-steps.txt</font>.",
     "Insist on ONE sentence — students who rewrite half can't read their own diff."),
    ("2.7", "Which Version Online?",
     "After committing, GitHub still shows the first version. "
     "Committing changes local; only pushing changes GitHub. Cycle runs twice to reinforce.",
     "The gap between committing and pushing is the most common beginner surprise."),
    ("2.8", "Fresh Session Pickup",
     "New agent session reads <font name='Courier' size='6.5'>next-steps.txt</font> to continue. "
     "<b><i>\"Memory is not a file.\"</i></b> Saved text persists; chat memory does not.",
     "This screen justifies the whole meeting — watch a new session read their own note."),
    ("2.9", "Explain the Workflow",
     "<b>Save</b> = updates file. <b>Commit</b> = records locally. <b>Push</b> = sends to GitHub. "
     "Document where work lives, what changed, next task.",
     "Ask three students to point at where their work lives and say the three words in order."),
]

def make_slide_rows(slides):
    rows = []
    for num, title, desc, note in slides:
        p = Paragraph(
            f"<b>{num} {title}</b> — {desc}",
            slide_style,
        )
        rows.append(p)
        if note:
            rows.append(Paragraph(f"↳ {note}", note_style))
    return rows

def lec_header(color, text):
    data = [[Paragraph(text, lec_header_style)]]
    t = Table(data, colWidths=[7.6*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("LEFTPADDING",  (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING",   (0,0), (-1,-1), 3),
        ("BOTTOMPADDING",(0,0), (-1,-1), 3),
    ]))
    return t

story = []

story.append(Paragraph("Week 2 Study Guide: Agent Foundations & Human Review", title_style))
story.append(Paragraph(
    "Lecture 1: Agent Foundations (Slides 1.1–1.17) &nbsp;|&nbsp; "
    "Lecture 2: Git &amp; GitHub Workflow (Slides 2.1–2.9) &nbsp;|&nbsp; "
    "Bold = key term &nbsp;·&nbsp; <i>Italic note</i> = instructor note",
    sub_style,
))
story.append(HRFlowable(width="100%", thickness=1, color=NAVY, spaceAfter=3))

story.append(lec_header(NAVY, "LECTURE 1 — Agent Foundations &amp; Human Review  (17 slides)"))
story.append(Spacer(1, 3))

l1_rows = make_slide_rows(LECTURE_1)
for item in l1_rows:
    story.append(item)

story.append(Spacer(1, 5))
story.append(lec_header(TEAL, "LECTURE 2 — Git &amp; GitHub Workflow  (9 slides)"))
story.append(Spacer(1, 3))

l2_rows = make_slide_rows(LECTURE_2)
for item in l2_rows:
    story.append(item)

story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=0.5, color=MGRAY, spaceAfter=2))
story.append(Paragraph(
    "<b>Key terms:</b> Agent = model that can look + loop + stop &nbsp;·&nbsp; "
    "Skill = reusable procedure &nbsp;·&nbsp; Tool = one action, one result &nbsp;·&nbsp; "
    "Agent Brief = Outcome · Evidence · Limits · Stop Rule &nbsp;·&nbsp; "
    "Trace = record that hides nothing &nbsp;·&nbsp; "
    "Save → Commit → Push",
    ParagraphStyle("Footer", parent=styles["Normal"],
                   fontSize=6.5, leading=8.5, textColor=colors.HexColor("#333333"),
                   fontName="Helvetica", alignment=TA_CENTER)
))

doc.build(story)
print(f"PDF saved to {OUTPUT}")
