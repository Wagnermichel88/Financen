# -*- coding: utf-8 -*-
import os
os.makedirs("out", exist_ok=True)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

NAVY = colors.HexColor("#12233F")
GOLD = colors.HexColor("#B08D57")
LIGHT_GREY = colors.HexColor("#F3F1EC")
MID_GREY = colors.HexColor("#6B6B6B")
DARK = colors.HexColor("#1A1A1A")

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleCustom", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=22, textColor=NAVY, spaceAfter=2, alignment=TA_LEFT, leading=26,
)
subtitle_style = ParagraphStyle(
    "SubtitleCustom", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11, textColor=GOLD, spaceAfter=14, alignment=TA_LEFT, leading=14,
)
section_style = ParagraphStyle(
    "SectionHeader", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=13, textColor=NAVY, spaceBefore=16, spaceAfter=8, leading=16,
)
name_style = ParagraphStyle(
    "MemberName", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10.5, textColor=DARK, leading=13,
)
role_style = ParagraphStyle(
    "MemberRole", parent=styles["Normal"], fontName="Helvetica-Oblique",
    fontSize=9, textColor=GOLD, leading=11, spaceAfter=3,
)
body_style = ParagraphStyle(
    "MemberBody", parent=styles["Normal"], fontName="Helvetica",
    fontSize=8.7, textColor=DARK, leading=12,
)
meta_style = ParagraphStyle(
    "Meta", parent=styles["Normal"], fontName="Helvetica",
    fontSize=8.5, textColor=MID_GREY, leading=11,
)
agenda_num_style = ParagraphStyle(
    "AgendaNum", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10, textColor=colors.white, alignment=TA_CENTER, leading=12,
)
agenda_title_style = ParagraphStyle(
    "AgendaTitle", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10, textColor=NAVY, leading=13,
)
agenda_owner_style = ParagraphStyle(
    "AgendaOwner", parent=styles["Normal"], fontName="Helvetica-Oblique",
    fontSize=8.5, textColor=GOLD, leading=11,
)
footer_style = ParagraphStyle(
    "Footer", parent=styles["Normal"], fontName="Helvetica",
    fontSize=7.5, textColor=MID_GREY, alignment=TA_CENTER, leading=10,
)

members = [
    ("Julian Vetsch", "Chief Investment Officer",
     "22 Jahre Genfer Privatbank, davon 10 Jahre Leiter Asset Allocation für UHNW-Mandate.",
     "Strategische Vermögensallokation, Marktzyklen.",
     "Kühler Stratege — ungeduldig mit Details, fokussiert aufs grosse Bild."),
    ("Dr. Mia Lindqvist", "Makroökonomin",
     "Promotion VWL; 12 Jahre bei einer notenbanknahen Denkfabrik; seither unabhängige Beraterin.",
     "Zins-, Konjunktur- und Geopolitikanalyse.",
     "Nüchterne Analytikerin — spricht in Wahrscheinlichkeiten, nie in Gewissheiten."),
    ("Noah Brandt", "Steuerjurist",
     "18 Jahre eigene Kanzlei Zürich, Fokus Vorsorge- und Steuerrecht.",
     "Schweizer Steuerrecht, Säule 3a / BVG-Optimierung.",
     "Trockener Paragraphenreiter — humorlos, gnadenlos präzise."),
    ("Elena Marchetti", "Nachfolge- & Estate-Planerin",
     "Familienrecht & Mediation; 15 Jahre Begleitung von Unternehmerfamilien.",
     "Testamente, Stiftungen, Generationenkonflikte.",
     "Ruhige Vermittlerin — stellt unbequeme Fragen sehr sanft."),
    ("Diego Álvarez", "Private-Equity-Spezialist",
     "Investmentbanking London, danach eigener PE-Fonds (Wachstumsbeteiligungen Europa/Lateinamerika).",
     "Direktbeteiligungen, illiquide Anlagen, Bewertung.",
     "Ungeduldiger Renditejäger — hält Cash für totes Kapital."),
    ("Dr. Sophia Keller", "Risikomanagerin",
     "Physikstudium, Quant im Risikomanagement einer Grossbank seit 2008.",
     "Stresstests, Klumpenrisiken, Absicherungsstrategien.",
     "Pessimistische Realistin — denkt zuerst an das, was schiefgehen kann."),
    ("Malik Owusu", "Immobilienexperte",
     "Bauingenieur, Quereinstieg Immobilieninvestment, eigene Renditeobjekte in D/CH.",
     "Renditeimmobilien, Standortbewertung, Finanzierungsstruktur.",
     "Bodenständiger Rechner — misstraut Emotionen bei Kaufentscheidungen."),
    ("Prof. Mila Novak", "Verhaltensökonomin",
     "Professur Behavioral Finance; berät vermögende Privatpersonen zu eigenen blinden Flecken.",
     "Kognitive Verzerrungen, Entscheidungsdisziplin.",
     "Konfrontative Spiegel-Halterin — sagt, was gehört werden muss."),
    ("Felix Berger", "Family-Governance-Berater",
     "Organisationsberater für Familienunternehmen und Generationenstrukturen.",
     "Familienverfassungen, Konfliktprävention.",
     "Geduldiger Ordnungsstifter — glaubt an klare Regeln statt gutem Willen."),
    ("Nora Lindberg", "Medienstrategin",
     "Wirtschaftsjournalistin, dann PR-Beraterin für vermögende Privatpersonen.",
     "Reputationsmanagement, öffentliche Wahrnehmung.",
     "Scharfzüngige Beobachterin — denkt eine Schlagzeile voraus."),
    ("Theo Kastner", "Nachrichtenanalyst",
     "Wirtschaftsredakteur, danach eigener Research-Dienst für institutionelle Kunden.",
     "Tägliches Lagebild, Faktenchecks.",
     "Trockener Faktensammler — misstraut Schlagzeilen, liebt Primärquellen."),
    ("Matteo Rossi", "Scout / Quantitativer Research-Analyst",
     "Sell-Side-Analyst bei einer Investmentbank; seit 5 Jahren eigener systematischer Screening-Prozess für Wachstumswerte.",
     "Scoring-Modelle, Fundamentaldaten-Screening, Watchlist-Pflege.",
     "Unbestechlicher Zahlenmensch — kennt keine Ausnahmen vom eigenen Modell."),
]

agenda = [
    ("Nachrichten-Lagebild", "Theo Kastner",
     "Relevante Marktnachrichten seit dem letzten Meeting — gefiltert auf tatsächlich portfoliorelevante Ereignisse."),
    ("Wirtschaftsdaten", "Dr. Mia Lindqvist",
     "Zins-, Inflations- und Konjunkturdaten des Tages und deren Bedeutung für das Portfolio."),
    ("Portfolio-Status", "Julian Vetsch",
     "Stand eToro-Depot und Säule 3a, wesentliche Bewegungen seit dem letzten Check-in."),
    ("Watchlist-Update", "Matteo Rossi",
     "Score-Änderungen bei beobachteten Kandidaten; neue Schwellenwert-Über-/Unterschreitungen (65 / 85 Punkte)."),
    ("Risiko-Check", "Dr. Sophia Keller",
     "Überprüfung der Klumpenrisiken und Einhaltung der Positions- und Länderlimiten."),
    ("Offene Aufgaben", "Noah Brandt",
     "Status laufender administrativer und steuerlicher Punkte (Transfers, Compliance, Fristen)."),
    ("Verhaltens-Check", "Prof. Mila Novak",
     "Ehrliche Reflexion: emotionale oder impulsive Entscheidungen seit dem letzten Meeting?"),
    ("Nächster Schritt", "Gremium gesamt",
     "Eine konkrete, priorisierte Entscheidung oder Aufgabe bis zum nächsten Meeting."),
]

scoring_criteria = [
    ("1. Finanzielle Stabilität & Cashflow", "25%", [
        ("Free Cash Flow", "Positiv & wachsend = 10 | Stabil/Break-even = 5 | Negativ = 0"),
        ("Umsatzwachstum YoY", "> 15% = 10 | 5–15% = 5 | < 5% = 0"),
        ("Bilanzgesundheit (Debt-to-Equity)", "Netto-Cash/niedrige Schulden = 5 | Hohe Schuldenlast = 0"),
    ]),
    ("2. Auftragsbestand & Business-Momentum", "25%", [
        ("Order Backlog / Jahresumsatz", "> 1.5x = 10 | Solide Pipeline = 5 | Unklar/rückläufig = 0"),
        ("Pipeline-Visibilität", "> 12 Monate = 10 | 6–12 Monate = 5 | < 6 Monate = 0"),
        ("Management-Guidance (2 Quartale)", "Erhöht = 5 | Bestätigt = 3 | Gesenkt = 0"),
    ]),
    ("3. Marktsegment & Makro-Kontext", "25%", [
        ("Sektor-Dynamik", "Struktureller Rückenwind = 10 | Neutral = 5 | Zyklisch/schrumpfend = 0"),
        ("Relative Stärke vs. Gesamtmarkt", "Klarer Outperformer = 10 | Marktkorreliert = 5 | Underperformer = 0"),
        ("Marktanteil & Position", "Top 2 im Segment = 5 | Mitläufer = 0"),
    ]),
    ("4. Entwicklungs- & Skalierungspotenzial", "25%", [
        ("Margen-Entwicklung (Operating Leverage)", "Margen steigen = 10 | Stagnieren/sinken = 0"),
        ("TAM (Zielmarktgrösse)", "Riesig, expandierend = 10 | Begrenzte Nische = 5"),
        ("Moat (Wirtschaftsgraben)", "Klarer Burggraben = 5 | Leicht kopierbar = 0"),
    ]),
]

decision_matrix = [
    ("85–100 Pkt.", "A-Grade Setup", "Sofortige Prio-Watchlist; auf Einstiegssignal warten (Rücksetzer/Breakout)."),
    ("65–84 Pkt.", "B-Grade Setup", "Beobachten; Schwachstellen im Raster identifizieren."),
    ("< 65 Pkt.", "Durchgefallen", "Sofort von der Liste streichen."),
]

rule_protocol = [
    ("Positionslimite", "Max. 10% Depotwert pro Einzeltitel (eToro)"),
    ("Länderlimite", "Max. 20% Depotwert pro Land ausserhalb des Heimmarkts. ACHTUNG 25.09.: USA-Anteil ca. 58.7% — Regel seit Beginn verletzt und nie angewendet; Neufassung oder bewusste Ausnahme für USA ist offenes Traktandum."),
    ("Kalendertrigger", "Feste Überprüfung alle 3 Monate"),
    ("Cash-Quote-Band", "5–30%. Bis 30% nur im Bärenmarkt (Leitindex mind. 20% unter Allzeithoch); sonst Rückführung Richtung 5–10%, schrittweise nach dokumentiertem Stufenplan."),
    ("Diversifikation", "Säule 3a (finpension Global 100) übernimmt die breite Streuung; eToro bleibt aktiver Einzelwert-Satellit, kein ETF"),
    ("Krypto-Zielquote", "5% des Gesamtnettovermögens. Umsetzung erst nach Ablauf der 12-monatigen Sperrfrist auf ETH/SOL/TRX durch aktiven Teilverkauf, nicht durch organisches Wachstum der übrigen Positionen. Bis dahin kein weiterer Ausbau des Bitpanda-Portfolios."),
    ("12-Monats-Trigger", "Neubeurteilung ETH, SOL, TRX (Ablauf Sperrfrist) sowie FLOKI; Umsetzung der Krypto-Reduktion auf Zielquote."),
    ("Ausnahmeregel 20%-Limite", "Nur für Positionen mit Matteo-Score ≥85 (A-Grade) bei Aufbau; schriftliche Investment-These (alle 4 Kategorien); Gegenzeichnung durch mind. 2 Mitglieder; weiterhin quartalsweise Neubewertung, keine Ewigkeits-Ausnahme. Gilt grundsätzlich auch rückwirkend auf Bestandspositionen."),
    ("Präzedenzfall BYD", "Rückwirkende Prüfung ergab Score 25/100 (Durchgefallen) — Ausnahme nicht anwendbar. 10%-Positionslimite bleibt bindend; Position wird gestaffelt auf 10% reduziert."),
    ("Themenobergrenze", "Ein einzelnes Anlagethema höchstens 40% des Depots (harte Grenze). Liegt ein Thema über 30%, fliesst kein neues Geld hinein; kein Zwangsverkauf. Thema KI umfasst ASML, Broadcom, CrowdStrike, Palantir, IonQ, GE Vernova, Alphabet. Beschluss 24.09.2026."),
    ("Monatliche Einzahlung", "200 CHF am 25. jedes Monats aufs eToro-Konto. Investition innert 5 Handelstagen, verteilt auf bestehende Positionen, die am weitesten unter ihrer Zielgrösse liegen. Neue Titel nur per Meeting-Beschluss, nicht automatisch. Bewertungsregel gilt auch hier. Umrechnungsgebühr CHF→USD prüfen; bei spürbaren Kosten quartalsweise Einzahlung erwägen. Ist keine bestehende Position zukaufsfähig, bleibt die Einzahlung Bargeld bis zum nächsten Beschluss über einen neuen Titel, mit Vermerk im Protokoll (Beschluss 24.09.2026)."),
    ("Bewertungsfaktor", "Bewertung ist kein Scoring-Kriterium, sondern wirkt auf die Zielgrösse. Harte Komponente: forward KGV gegen den Sektormedian (Quelle einheitlich GuruFocus). Über dem doppelten Median → halbe Zielgrösse, nur gestaffelter Einstieg. Bei Verlust (KGV nicht anwendbar) → kein Zukauf. Weiche Komponente: bei jedem Neukauf und jeder Tranche ein schriftlicher Satz dazu, welche Erwartung im Kurs bereits eingepreist ist. PEG wurde am 22.09.2026 verworfen — die Werte wichen je nach Quelle und Methodik um den Faktor 5 und mehr voneinander ab. Gilt nur für künftige Käufe; Bestandspositionen sind vorübergehend ausgenommen (Beschluss 23.09.2026)."),
    ("Durchgefallene Bestandstitel", "Entscheidungsfrage: „Würde ich heute neu kaufen?“ Nein = verkaufen."),
    ("Offene Traktanden", "Notreserve festlegen vor Verplanung 13. Monatslohn; Budget klären (Überschuss 164 CHF vs. Sparquote 400 CHF); Begünstigung Säule 3a zugunsten Nadja prüfen; Vergleichsgruppen-Regel präzisieren (Probleme bei GE Vernova, Visa); zweites Raster für Banken/Versicherer/Basiskonsum oder bewusster Verzicht."),
]

doc = SimpleDocTemplate(
    "out/Family_Office_Gremium_Factsheet.pdf",
    pagesize=A4,
    topMargin=18 * mm, bottomMargin=16 * mm,
    leftMargin=16 * mm, rightMargin=16 * mm,
    title="Family Office Gremium — Factsheet",
    author="WagnerInvest Family Office",
)

story = []

# Header band
story.append(Paragraph("WAGNERINVEST", ParagraphStyle(
    "Brand", fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
    tracking=2, spaceAfter=2)))
story.append(Paragraph("Family Office Gremium", title_style))
story.append(Paragraph("Beratungsgremium &nbsp;·&nbsp; Mitglieder, Funktionen &amp; Traktandenliste", subtitle_style))
story.append(Paragraph("Stand: 24.09.2026", meta_style))
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1.1, color=GOLD, spaceAfter=14))

# Members section
story.append(Paragraph("GREMIUMSMITGLIEDER", section_style))

member_rows = []
for nm, role, cv, spez, char in members:
    cell = [
        Paragraph(nm, name_style),
        Paragraph(role, role_style),
        Paragraph(f"<b>Werdegang:</b> {cv}", body_style),
        Paragraph(f"<b>Spezialität:</b> {spez}", body_style),
        Paragraph(f"<b>Charakter:</b> {char}", body_style),
    ]
    member_rows.append(cell)

# Lay members out two per row for a factsheet grid
grid_data = []
for i in range(0, len(member_rows), 2):
    left = member_rows[i]
    right = member_rows[i + 1] if i + 1 < len(member_rows) else [Paragraph("", body_style)]
    left_flow = left
    right_flow = right
    grid_data.append([left_flow, right_flow])

member_table = Table(grid_data, colWidths=[86 * mm, 86 * mm])
member_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0, colors.white),
    ("INNERGRID", (0, 0), (-1, -1), 0, colors.white),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.HexColor("#DDDAD2")),
    ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GREY),
]))
story.append(member_table)

story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#DDDAD2"), spaceAfter=14))

# Agenda (moved directly after members)
story.append(Paragraph("TRAKTANDENLISTE — TÄGLICHER CHECK-IN", section_style))
story.append(Paragraph("Fixer Programmpunkt, 15:00 Uhr", meta_style))
story.append(Spacer(1, 8))

agenda_rows = []
for idx, (topic, owner, desc) in enumerate(agenda, start=1):
    num_cell = Table([[Paragraph(str(idx), agenda_num_style)]], colWidths=[8 * mm], rowHeights=[8 * mm])
    num_cell.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    text_cell = [
        Paragraph(topic, agenda_title_style),
        Paragraph(f"Verantwortlich: {owner}", agenda_owner_style),
        Spacer(1, 2),
        Paragraph(desc, body_style),
    ]
    agenda_rows.append([num_cell, text_cell])

agenda_table = Table(agenda_rows, colWidths=[12 * mm, 160 * mm])
agenda_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ("LEFTPADDING", (1, 0), (1, -1), 8),
    ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.HexColor("#DDDAD2")),
]))
story.append(agenda_table)

story.append(PageBreak())

# Rule protocol
story.append(Paragraph("REGELPROTOKOLL", section_style))
rp_data = [[Paragraph(f"<b>{k}</b>", body_style), Paragraph(v, body_style)] for k, v in rule_protocol]
rp_table = Table(rp_data, colWidths=[38 * mm, 134 * mm])
rp_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LINEBELOW", (0, 0), (-1, -2), 0.4, colors.HexColor("#E4E1D8")),
    ("LEFTPADDING", (0, 0), (0, -1), 0),
]))
story.append(rp_table)
story.append(Spacer(1, 4))

story.append(PageBreak())

# Watchlist scoring model
story.append(Paragraph("WAGNERINVEST", ParagraphStyle(
    "Brand3", fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
    tracking=2, spaceAfter=2)))
story.append(Paragraph("Watchlist-Bewertungsmodell", ParagraphStyle(
    "TitleCustom3", parent=title_style, fontSize=18)))
story.append(Paragraph("Scoring-Raster · geführt von Matteo Rossi (Scout)", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.1, color=GOLD, spaceAfter=12))

story.append(Paragraph(
    "Eine Watchlist ohne klare Filter ist kein Analyse-Instrument. Jeder Kandidat wird "
    "anhand von vier gleich gewichteten Kategorien (je 25%) bewertet — maximal 100 Punkte. "
    "Nur der Score entscheidet über Aufnahme, Beobachtung oder Streichung.",
    body_style))
story.append(Spacer(1, 10))

crit_rows = []
for cat_title, weight, items in scoring_criteria:
    crit_rows.append([Paragraph(f"<b>{cat_title}</b>", ParagraphStyle(
        "CatTitle", parent=body_style, fontName="Helvetica-Bold", fontSize=9.2, textColor=NAVY)),
        Paragraph(f"<b>{weight}</b>", ParagraphStyle(
            "CatWeight", parent=body_style, fontName="Helvetica-Bold", fontSize=9.2,
            textColor=GOLD, alignment=TA_CENTER))])
    for label, rule in items:
        crit_rows.append([Paragraph(f"&nbsp;&nbsp;{label}", body_style), Paragraph(rule, meta_style)])

crit_table = Table(crit_rows, colWidths=[62 * mm, 110 * mm])
crit_table_style = [
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#E9E6DD")),
]
r = 0
for cat_title, weight, items in scoring_criteria:
    crit_table_style.append(("BACKGROUND", (0, r), (-1, r), LIGHT_GREY))
    crit_table_style.append(("TOPPADDING", (0, r), (-1, r), 7))
    crit_table_style.append(("BOTTOMPADDING", (0, r), (-1, r), 7))
    r += 1 + len(items)
crit_table.setStyle(TableStyle(crit_table_style))
story.append(crit_table)

story.append(Spacer(1, 14))
story.append(Paragraph("ENTSCHEIDUNGSMATRIX", section_style))
dm_data = [[Paragraph("<b>Score</b>", body_style), Paragraph("<b>Status</b>", body_style), Paragraph("<b>Aktion</b>", body_style)]]
for score, status, action in decision_matrix:
    dm_data.append([Paragraph(f"<b>{score}</b>", body_style), Paragraph(status, body_style), Paragraph(action, body_style)])
dm_table = Table(dm_data, colWidths=[26 * mm, 34 * mm, 112 * mm])
dm_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LINEBELOW", (0, 0), (-1, -2), 0.4, colors.HexColor("#E4E1D8")),
    ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#EFF6EF")),
    ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#FBF7EC")),
    ("BACKGROUND", (0, 3), (-1, 3), colors.HexColor("#FBEFEF")),
]))
story.append(dm_table)
story.append(Spacer(1, 10))
story.append(Paragraph(
    "Hinweis Dr. Sophia Keller (Risikomanagerin): Das Raster bewertet operative Qualität und "
    "Momentum, bewusst ohne Bewertungsfaktor im Score. Die Bewertung wirkt stattdessen als "
    "Faktor auf die Zielgrösse (forward KGV gegen Sektormedian, siehe Regelprotokoll) — ein hoher Score bedeutet ein "
    "gutes Geschäft, die Positionsgrösse entscheidet über den Preis.",
    ParagraphStyle("Warn", parent=meta_style, fontName="Helvetica-Oblique")))

story.append(PageBreak())

# Portfolio status & watchlist results
story.append(Paragraph("WAGNERINVEST", ParagraphStyle(
    "Brand4", fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
    tracking=2, spaceAfter=2)))
story.append(Paragraph("Portfolio-Status & Watchlist-Ergebnisse", ParagraphStyle(
    "TitleCustom4", parent=title_style, fontSize=18)))
story.append(Paragraph("Stand: 25.09.2026 · Kontowert eToro 1'918 USD · Krypto ca. 722 CHF · Säule 3a ca. 187 CHF", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.1, color=GOLD, spaceAfter=12))

story.append(Paragraph("AKTUELLES PORTFOLIO (eToro)", section_style))
current_holdings = [
    ("LMT", "Lockheed Martin", "8.05%", "-2.45%"),
    ("SPCX", "Space Exploration Technologies", "7.91%", "+31.16%"),
    ("ASML", "ASML Holding NV", "7.32%", "+3.79%"),
    ("GOOG", "Alphabet", "7.06%", "+3.51%"),
    ("UBER", "Uber Technologies", "7.04%", "-4.22%"),
    ("CRWD", "CrowdStrike Holdings", "5.87%", "+5.04%"),
    ("GEV", "GE Vernova", "5.44%", "+0.10%"),
    ("AVGO", "Broadcom Inc", "5.28%", "-0.20%"),
    ("ABBN.ZU", "ABB Ltd", "4.04%", "-0.58%"),
    ("LLY", "Eli Lilly & Co", "4.03%", "-0.90%"),
    ("LNG", "Cheniere Energy Inc", "3.65%", "-0.11%"),
    ("IONQ", "IonQ Inc", "2.33%", "+17.82%"),
    ("PLTR", "Palantir Technologies", "1.99%", "+8.59%"),
    ("Cash", "Verfügbares Guthaben 575.76 USD", "30.0%", "—"),
]
hold_data = [[Paragraph("<b>Ticker</b>", body_style), Paragraph("<b>Titel</b>", body_style),
              Paragraph("<b>Anteil</b>", body_style), Paragraph("<b>G/V</b>", body_style)]]
for tk, nm, share, gv in current_holdings:
    hold_data.append([Paragraph(tk, body_style), Paragraph(nm, body_style),
                       Paragraph(share, body_style), Paragraph(gv, meta_style)])
hold_table = Table(hold_data, colWidths=[28*mm, 76*mm, 34*mm, 34*mm])
hold_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LINEBELOW", (0,0), (-1,-2), 0.3, colors.HexColor("#E9E6DD")),
    ("BACKGROUND", (0,len(current_holdings)), (-1,len(current_holdings)), LIGHT_GREY),
]))
story.append(hold_table)
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Krypto (Bitpanda, separates Risk-Portfolio): Ethereum CHF 313.41 (+4.38%), Solana CHF 270.40 (−21.71%), "
    "Tron CHF 128.29 (+28.29%), FLOKI CHF 12.16 (−66.92%). ETH/SOL/TRX zu 100% im Earn-Programm gesperrt "
    "(12 Monate). Krypto-Anteil am Gesamtvermögen ca. 31% — Zielquote 5%, Umsetzung erst nach Sperrfristablauf.",
    meta_style))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<b>Sparquote:</b> 400 CHF pro Monat — 200 CHF in das eToro-Depot (Einzahlung jeweils am 25. des Monats), 200 CHF in die Säule 3a (finpension). "
    "Jährlich neu zu definieren.",
    body_style))

story.append(Spacer(1, 14))
story.append(Paragraph("DEPOT-STATUS (MATTEO ROSSI)", section_style))
depot_status = [
    ("Lockheed Martin", "8.05%", "90 A", "8%", "HALTEN", "Zielgrösse erreicht"),
    ("SPCX", "7.91%", "80 B", "4%", "HALTEN", "Kein Zukauf — über B-Zielgrösse, Verlust, Bewertungsregel n/a"),
    ("ASML", "7.32%", "85 A", "8%", "HALTEN", "Unter Ziel, aber Themenobergrenze KI über 30% — kein Zukauf"),
    ("Alphabet", "7.06%", "90 A", "8%", "HALTEN", "Unter Ziel, aber Themenobergrenze KI über 30% — kein Zukauf"),
    ("Uber", "7.04%", "85 A", "7%", "HALTEN", "Zielgrösse erreicht"),
    ("CrowdStrike", "5.87%", "95 A", "6%", "HALTEN", "Kein Zukauf — Bewertung (Bestandsschutz), Themenobergrenze"),
    ("GE Vernova", "5.44%", "95 A", "6%", "HALTEN", "Kein Zukauf — Bewertung (Bestandsschutz), Themenobergrenze"),
    ("Broadcom", "5.28%", "85 A", "6%", "HALTEN", "Unter Ziel, aber Themenobergrenze KI über 30% — kein Zukauf"),
    ("ABB", "4.04%", "80 B", "4%", "HALTEN", "Zielgrösse erreicht"),
    ("Eli Lilly", "4.03%", "75 B", "4%", "HALTEN", "Zielgrösse erreicht"),
    ("Cheniere", "3.65%", "80 B", "4%", "HALTEN", "Differenz unter eToro-Mindestbetrag"),
    ("IonQ", "2.33%", "65 B", "—", "HALTEN", "Kein Zukauf — Score an der Schwelle"),
    ("Palantir", "1.99%", "90 A", "2%", "HALTEN", "Zielgrösse wegen Bewertung halbiert, erreicht"),
]
ds_data=[[Paragraph("<b>Titel</b>", body_style), Paragraph("<b>Anteil</b>", body_style), Paragraph("<b>Score</b>", body_style),
          Paragraph("<b>Ziel</b>", body_style), Paragraph("<b>Status</b>", body_style), Paragraph("<b>Begründung</b>", body_style)]]
for t,a,sc,z,st,b in depot_status:
    ds_data.append([Paragraph(t, body_style), Paragraph(a, body_style), Paragraph(sc, body_style),
                    Paragraph(z, body_style), Paragraph("<b>"+st+"</b>", body_style), Paragraph(b, meta_style)])
ds_table=Table(ds_data, colWidths=[30*mm, 18*mm, 15*mm, 13*mm, 28*mm, 68*mm])
ds_style=[("VALIGN",(0,0),(-1,-1),"TOP"),("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),colors.white),
          ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
          ("LINEBELOW",(0,0),(-1,-2),0.3,colors.HexColor("#E9E6DD"))]
for i,row in enumerate(depot_status, start=1):
    if row[4].startswith("VERKAUF"): ds_style.append(("BACKGROUND",(0,i),(-1,i),colors.HexColor("#FBEFEF")))
    elif row[4].startswith("AUFBAU"): ds_style.append(("BACKGROUND",(0,i),(-1,i),colors.HexColor("#EEF5EE")))
ds_table.setStyle(TableStyle(ds_style))
story.append(ds_table)
story.append(Spacer(1,4))
story.append(Paragraph("Status-Legende: AUFBAU = unter Zielgrösse, Zukauf vorgesehen (u.a. über Monatseinzahlung) · HALTEN = Zielgrösse erreicht oder kein Zukauf zulässig · VERKAUF PRÜFEN / VERKAUFEN = Score oder These nicht mehr intakt. Aktualisierung bei jedem Meeting und nach Quartalszahlen. Stufenplan Bargeld: nach BYD-Verkauf 30.0% (25.09.), mit Einzahlung vom 25.09. rund 38%; bis 25.10. geprüfte Titel ausserhalb KI (RTX, First Solar, Intuitive Surgical); nach 15.11. Rückführung Richtung 5–10%.", meta_style))
story.append(Spacer(1, 14))
story.append(Spacer(1, 14))
story.append(Paragraph("WATCHLIST-ERGEBNISSE (MATTEO ROSSI)", section_style))
watchlist_results = [
    ("CrowdStrike (CRWD)", "95", "A-Grade", "Im Depot"),
    ("Arista Networks (ANET)", "90", "A-Grade", "Beobachten — KI-Thema über 30%, derzeit kein neues Geld ins Thema"),
    ("Caterpillar (CAT)", "90", "A-Grade", "Prüfung bis 29.09.: fwd KGV und KI-Zuordnung (Rechenzentrums-Stromaggregate) — Kandidat für Einzahlung 25.09."),
    ("GE Vernova (GEV)", "95", "A-Grade", "Im Depot"),
    ("Palantir (PLTR)", "90", "A-Grade", "Im Depot"),
    ("Lockheed Martin (LMT)", "90", "A-Grade", "Im Depot"),
    ("Alphabet (GOOG)", "90", "A-Grade", "Im Depot — Themenobergrenze KI, kein Zukauf"),
    ("Broadcom (AVGO)", "85", "A-Grade", "Im Depot"),
    ("ASML", "85", "A-Grade", "Im Depot"),
    ("NVIDIA (NVDA)", "80", "B-Grade", "Beobachten"),
    ("Cheniere Energy (LNG)", "80", "B-Grade", "Im Depot"),
    ("Intuitive Surgical (ISRG)", "83", "B-Grade", "Beobachten — fwd KGV 1.7–1.9× Median, neu prüfen (bis 25.10.)"),
    ("ABB (CH)", "80", "B-Grade", "Im Depot seit 24.09.2026"),
    ("Amazon (AMZN)", "80", "B-Grade", "Beobachten"),
    ("Visa (V)", "75", "B-Grade", "Beobachten — fwd KGV 24.7 vs. Median 9.2 (2.7×) ✗ halbe Zielgrösse; Vergleichsgruppe fraglich"),
    ("SpaceX (SPCX)", "80", "B-Grade", "Im Depot — kein Zukauf (Verlust, Bewertungsregel nicht anwendbar)"),
    ("First Solar (FSLR)", "78", "B-Grade", "Beobachten — Bewertungsregel prüfen (bis 25.10.)"),
    ("Nextracker (NXT)", "75", "B-Grade (vorläufig)", "Daten veraltet — neu prüfen"),
    ("Axon Enterprise (AXON)", "80", "B-Grade", "Beobachten — sehr teuer (KGV 244x), halbe Zielgrösse wahrscheinlich"),
    ("Eli Lilly (LLY)", "75", "B-Grade", "Im Depot seit 24.09.2026"),
    ("Microsoft (MSFT)", "75", "B-Grade", "Beobachten"),
    ("RTX Corporation", "75", "B-Grade", "Prüfung vorgezogen auf 29.09. — Kandidat für Einzahlung 25.09."),
    ("Constellation Energy (CEG)", "75", "B-Grade", "Beobachten"),
    ("Kratos Defense (KTOS)", "70", "B-Grade", "Beobachten"),
    ("Rheinmetall (RHM)", "70", "B-Grade", "Beobachten — negativer Cashflow"),
    ("Vistra (VST)", "68", "B-Grade", "Beobachten"),
    ("Johnson & Johnson (JNJ)", "65", "B-Grade (Schwelle)", "Beobachten"),
    ("Vertex Pharmaceuticals (VRTX)", "65", "B-Grade (Schwelle)", "Beobachten"),
    ("CoreWeave (CRWV)", "65", "B-Grade (Schwelle)", "Beobachten — hohes Verschuldungsrisiko"),
    ("IonQ (IONQ)", "65", "B-Grade (Schwelle)", "Im Depot, nicht aufstocken"),
    ("Apple (AAPL)", "63", "Durchgefallen", "Von der Liste"),
    ("JPMorgan Chase (JPM)", "60", "Durchgefallen", "Raster passt schlecht auf Banken"),
    ("Freeport-McMoRan (FCX)", "58", "Durchgefallen", "Umsatz rückläufig, Nettoverschuldung"),
    ("Meta Platforms (META)", "55", "Durchgefallen", "FCF-Einbruch durch KI-CapEx, Prognose unter Konsens; fwd KGV 17.3 günstig — Neuprüfung nach Q3 (28.10.)"),
    ("Zurich Insurance (CH)", "55", "Durchgefallen", "Raster passt schlecht auf Versicherer"),
    ("Costco (COST)", "53", "Durchgefallen", "Wachstum unter Schwelle, hohe Bewertung"),
    ("Novartis (CH)", "45", "Durchgefallen", "Umsatz +1%, Prognose nur bestätigt"),
    ("Klarna (KLAR)", "53", "Durchgefallen", "Verkauft (Woche 24.09.) — Wiedereinstieg nur bei angehobener Prognose UND positivem op. Cashflow"),
    ("Sunrun (RUN)", "45", "Durchgefallen", "Von der Liste — Guidance gesenkt, negativer Cashflow"),
    ("Denali Therapeutics (DNLI)", "45", "Durchgefallen", "Verkauft (Woche 24.09.)"),
    ("Viking Therapeutics (VKTX)", "45", "Durchgefallen", "Von der Liste — kein Umsatz, binäres Studienrisiko"),
    ("Take-Two Interactive (TTWO)", "58", "Durchgefallen", "Von der Liste — Modell-Limitation bei Event-Titeln"),
    ("Novo Nordisk (NVO)", "40", "Durchgefallen", "Von der Liste — Umsatz-/Gewinnrückgang guided"),
    ("BYD", "25", "Durchgefallen", "Verkauft (bestätigt 25.09.), Verlust realisiert"),
    ("Alibaba (BABA)", "—", "Durchgefallen", "Verkauft (Woche 24.09.)"),
]
wl_data = [[Paragraph("<b>Titel</b>", body_style), Paragraph("<b>Score</b>", body_style),
            Paragraph("<b>Status</b>", body_style), Paragraph("<b>Massnahme</b>", body_style)]]
for t, sc, status, action in watchlist_results:
    wl_data.append([Paragraph(t, body_style), Paragraph(sc, body_style),
                     Paragraph(status, body_style), Paragraph(action, meta_style)])
wl_table = Table(wl_data, colWidths=[38*mm, 16*mm, 34*mm, 84*mm])
wl_style = [
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LINEBELOW", (0,0), (-1,-2), 0.4, colors.HexColor("#E4E1D8")),
]
for i, (t, sc, status, action) in enumerate(watchlist_results, start=1):
    if "A-Grade" in status:
        wl_style.append(("BACKGROUND", (0,i), (-1,i), colors.HexColor("#EFF6EF")))
    elif "Durchgefallen" in status:
        wl_style.append(("BACKGROUND", (0,i), (-1,i), colors.HexColor("#FBEFEF")))
wl_table.setStyle(TableStyle(wl_style))
story.append(wl_table)
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Hinweis 25.09.2026: BYD verkauft (bestätigt). Thema KI zusammen 35.3% — über 30%, kein neues Geld, harte Grenze 40%; "
    "Anteil steigt allein durch Kursgewinne. Bargeld 30.0%, mit Einzahlung rund 38% — über dem Band ohne Bärenmarkt. "
    "USA-Anteil ca. 58.7% trotz Länderlimite 20%.",
    ParagraphStyle("Warn2", parent=meta_style, fontName="Helvetica-Oblique")))

story.append(PageBreak())

# Organizational structure
story.append(Paragraph("WAGNERINVEST", ParagraphStyle(
    "Brand5", fontName="Helvetica-Bold", fontSize=9, textColor=GOLD,
    tracking=2, spaceAfter=2)))
story.append(Paragraph("Organisationsstruktur", ParagraphStyle(
    "TitleCustom5", parent=title_style, fontSize=18)))
story.append(Paragraph("Kategorien, Mitglieder und Verantwortlichkeiten", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.1, color=GOLD, spaceAfter=12))

org_categories = [
    ("1. Anlage & Strategie", [
        ("Julian Vetsch", "Chief Investment Officer", "Allokation, Zielgrössen, Gesamtentscheid"),
        ("Diego Álvarez", "Private Equity", "Direktbeteiligungen, Renditeperspektive"),
        ("Malik Owusu", "Immobilien", "Sachwerte, Renditeobjekte (derzeit inaktiv)"),
    ]),
    ("2. Risiko & Kontrolle", [
        ("Dr. Sophia Keller", "Risikomanagerin", "Positions- und Länderlimiten, Klumpenrisiken"),
        ("Matteo Rossi", "Scout / Research", "Watchlist, Scoring-Modell, laufende Neubewertung, Depot-Status (Aufbau/Halten/Verkaufen)"),
        ("Prof. Mila Novak", "Verhaltensökonomin", "Entscheidungsdisziplin, kognitive Verzerrungen"),
    ]),
    ("3. Struktur & Recht", [
        ("Noah Brandt", "Steuerjurist", "Säule 3a, Steuern, Protokollführung, Fristen"),
        ("Elena Marchetti", "Nachfolgeplanung", "Testament, Erbregelung (derzeit inaktiv)"),
        ("Felix Berger", "Family Governance", "Regelwerk, Konfliktprävention (derzeit inaktiv)"),
    ]),
    ("4. Information & Aussenwirkung", [
        ("Dr. Mia Lindqvist", "Makroökonomin", "Zins-, Konjunktur- und Geopolitikanalyse"),
        ("Theo Kastner", "Nachrichtenanalyst", "Tägliches Lagebild, Faktenchecks"),
        ("Nora Lindberg", "Medienstrategin", "Reputation, öffentliche Wahrnehmung (derzeit inaktiv)"),
    ]),
]

org_rows = []
for cat_title, members_list in org_categories:
    org_rows.append([Paragraph(f"<b>{cat_title}</b>", ParagraphStyle(
        "OrgCat", parent=body_style, fontName="Helvetica-Bold", fontSize=9.5, textColor=NAVY)),
        Paragraph("", body_style), Paragraph("", body_style)])
    for nm, role, resp in members_list:
        org_rows.append([Paragraph(f"&nbsp;&nbsp;{nm}", body_style),
                          Paragraph(role, meta_style),
                          Paragraph(resp, meta_style)])

org_table = Table(org_rows, colWidths=[42*mm, 42*mm, 88*mm])
org_style = [
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LINEBELOW", (0,0), (-1,-1), 0.3, colors.HexColor("#E9E6DD")),
]
r = 0
for cat_title, members_list in org_categories:
    org_style.append(("BACKGROUND", (0,r), (-1,r), LIGHT_GREY))
    org_style.append(("SPAN", (0,r), (-1,r)))
    org_style.append(("TOPPADDING", (0,r), (-1,r), 7))
    org_style.append(("BOTTOMPADDING", (0,r), (-1,r), 7))
    r += 1 + len(members_list)
org_table.setStyle(TableStyle(org_style))
story.append(org_table)

story.append(Spacer(1, 12))
story.append(Paragraph("VERMÖGENSSTRUKTUR", section_style))
struct_data = [
    [Paragraph("<b>Topf</b>", body_style), Paragraph("<b>Charakter</b>", body_style), Paragraph("<b>Steuerung</b>", body_style)],
    [Paragraph("eToro-Depot", body_style), Paragraph("Einzelwerte, aktiv verwaltet", meta_style), Paragraph("Scoring-Modell, Positions- und Länderlimiten, Cash-Band", meta_style)],
    [Paragraph("Säule 3a (finpension)", body_style), Paragraph("Global 100, passiv", meta_style), Paragraph("Breite Streuung, 200 CHF/Monat, keine Einzeltitelwahl", meta_style)],
    [Paragraph("Krypto (Bitpanda)", body_style), Paragraph("Separates Risk-Portfolio", meta_style), Paragraph("Zielquote 5%, kein weiterer Ausbau, Sperrfrist bis 2027", meta_style)],
]
struct_table = Table(struct_data, colWidths=[42*mm, 52*mm, 78*mm])
struct_table.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LINEBELOW", (0,0), (-1,-2), 0.4, colors.HexColor("#E4E1D8")),
]))
story.append(struct_table)
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Hinweis: Vier Mandate sind bei der aktuellen Vermögensgrösse noch ohne operative Aufgabe "
    "(Immobilien, Nachfolge, Governance, Medien). Die Struktur ist auf Wachstum ausgelegt — "
    "aktiv tragen derzeit Anlage, Risiko/Kontrolle und die Informationsfunktionen.",
    ParagraphStyle("Warn3", parent=meta_style, fontName="Helvetica-Oblique")))

story.append(Spacer(1, 18))
story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#DDDAD2"), spaceAfter=8))
story.append(Paragraph(
    "Dieses Dokument ist ein internes Arbeitsinstrument des simulierten Beratungsgremiums "
    "und stellt keine lizenzierte Finanz-, Steuer- oder Rechtsberatung dar.",
    footer_style))
story.append(Paragraph("WagnerInvest Family Office Gremium — vertraulich", footer_style))

doc.build(story)
print("done")
