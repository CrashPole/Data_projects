import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────────
programs = [
    # (Label, Range km, IOC year, Status, DPS_Relevant)
    ("JSM (Belgium)", 560, 2028, "In Dev", True),
    ("NSM (Belgium)", 200, 2032, "In Dev", True),
    ("NSM (Bulgaria)", 200, 2030, "In Dev", False),
    ("Tomahawk (Canada)", 1600, 2035, "Aspirational", True),
    ("ATACMS M57 (Estonia)", 300, 2025, "Active", True),
    ("CTM-290 (Estonia)", 290, 2028, "In Dev", True),
    ("Blue Spear (Estonia)", 290, 2024, "Active", True),
    ("JASSM (Finland)", 370, 2018, "Active", True),
    ("JASSM-ER (Finland)", 925, 2028, "In Dev", True),
    ("AARGM-ER (Finland)", 300, 2028, "In Dev", True),
    ("SCALP-EG (France)", 560, 2004, "Active", True),
    ("MdCN/NCM (France)", 1000, 2017, "Active", True),
    ("ASMPA-R (France)", 600, 2023, "Active", True),
    ("ASN4G (France)", 1000, 2035, "In Dev", True),
    ("MBT (France)", 2000, 2035, "Aspirational", True),
    ("OWE (France)", 500, 2027, "In Dev", True),
    ("Chorus (France)", 3000, 2027, "In Dev", True),
    ("Taurus KEPD-350 (Germany)", 500, 2005, "Active", True),
    ("Taurus Neo (Germany)", 500, 2030, "In Dev", True),
    ("JSM (Germany)", 560, 2027, "In Dev", True),
    ("Tomahawk Typhon (Germany)", 1600, 2035, "Aspirational", True),
    ("Storm Shadow (Greece)", 560, 2004, "Active", True),
    ("ATACMS M39 (Greece)", 300, 1997, "Active", True),
    ("Predator Hawk (Greece)", 300, 2028, "In Dev", True),
    ("MdCN/NCM (Italy)", 1000, 2035, "Aspirational", True),
    ("SCALP-EG (Italy)", 560, 2006, "Active", True),
    ("Teseo MK2/E (Italy)", 350, 2027, "In Dev", True),
    ("AARGM-ER (Italy)", 300, 2028, "In Dev", True),
    ("ATACMS M57 (Latvia)", 300, 2028, "In Dev", True),
    ("ATACMS M57 (Lithuania)", 300, 2026, "In Dev", True),
    ("ELSA OWE 500+ (Multinational)", 500, 2035, "Aspirational", True),
    ("Deep Precision Strike (UK/DE)", 2000, 2035, "Aspirational", True),
    ("JASSM-ER (Netherlands)", 925, 2027, "In Dev", True),
    ("Tomahawk (Netherlands)", 1600, 2028, "In Dev", True),
    ("AARGM-ER (Netherlands)", 300, 2028, "In Dev", True),
    ("NSM (Norway)", 200, 2012, "Active", True),
    ("JSM (Norway)", 560, 2025, "Active", True),
    ("K239+CTM-290 (Norway)", 290, 2029, "In Dev", True),
    ("JASSM-ER (Poland)", 925, 2017, "Active", True),
    ("CTM-290 (Poland)", 290, 2027, "In Dev", True),
    ("ATACMS M57 (Poland)", 300, 2023, "Active", True),
    ("JASSM (Poland)", 370, 2017, "Active", True),
    ("ATACMS (Romania)", 300, 2022, "Active", True),
    ("Taurus KEPD-350 (Spain)", 500, 2009, "Active", True),
    ("RBS15 Mk4/Gungnir (Sweden)", 300, 2035, "In Dev", True),
    ("Taurus KEPD-350 (Sweden)", 500, 2028, "In Dev", True),
    ("SOM (Türkiye)", 250, 2018, "Active", False),
    ("Atmaca (Türkiye)", 220, 2021, "Active", False),
    ("Tayfun (Türkiye)", 750, 2023, "Active", True),
    ("Tayfun Blk 4 (Türkiye)", 1500, 2035, "Aspirational", True),
    ("Cenk (Türkiye)", 2000, 2035, "Aspirational", True),
    ("Gezgin (Türkiye)", 1000, 2035, "Aspirational", True),
    ("Yildirimhan (Türkiye)", 6000, 2035, "Aspirational", True),
    ("Storm Shadow (UK)", 560, 2003, "Active", True),
    ("Tomahawk (UK)", 1600, 2008, "Active", True),
    ("UK Hypersonic HTCDF", 2000, 2035, "Aspirational", False),
    ("Project Nightfall (UK)", 500, 2035, "Aspirational", True),
    ("PrSM Inc 1 (USA)", 500, 2023, "Active", True),
    ("LRHW Dark Eagle (USA)", 3500, 2026, "Active", True),
    ("MRC Typhon (USA)", 1600, 2023, "Active", True),
    ("ATACMS (USA)", 300, 1989, "Active", True),
    ("JASSM-ER (USA)", 1000, 2014, "Active", True),
    ("LRASM (USA)", 930, 2018, "Active", True),
    ("Tomahawk Blk V (USA)", 1600, 2021, "Active", True),
    ("LUCAS OWE (USA)", 822, 2025, "Active", True),
]

# ── Colours by status ─────────────────────────────────────────────────────────
color_map = {
    "Active":       "#2ecc71",
    "In Dev":       "#3498db",
    "Aspirational": "#e67e22",
}

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(22, 14))
fig.patch.set_facecolor("#0d1117")
ax.set_facecolor("#0d1117")

# Shade capability-gap bands on range axis
gap_bands = [
    (1050, 1550, "#ff4444", "Gap: 1,000–1,600 km\n(strategic reach)"),
    (1650, 2900, "#ff4444", "Gap: 1,600–3,000 km\n(theatre-ballistic)"),
]
for y0, y1, col, label in gap_bands:
    ax.axhspan(y0, y1, color=col, alpha=0.10, zorder=0)
    ax.text(2036.3, (y0 + y1) / 2, label, color="#ff6666",
            fontsize=7.5, va="center", style="italic")

# Scatter + labels
years = [p[2] for p in programs]
ranges = [p[1] for p in programs]
statuses = [p[3] for p in programs]
names = [p[0] for p in programs]

for name, yr, rng, status in zip(names, years, ranges, statuses):
    col = color_map[status]
    ax.scatter(yr, rng, color=col, s=60, zorder=3, alpha=0.92,
               edgecolors="white", linewidths=0.4)
    ax.annotate(name, xy=(yr, rng),
                xytext=(4, 2), textcoords="offset points",
                fontsize=5.8, color="#dddddd", alpha=0.88,
                fontfamily="monospace")

# Range-band guides
band_lines = [(200, "200 km — Anti-ship / short"),
              (500, "500 km — Theatre strike"),
              (1000, "1,000 km — Long-range cruise"),
              (1600, "1,600 km — Tomahawk-class"),
              (3000, "3,000 km — Strategic reach")]
for y, lbl in band_lines:
    ax.axhline(y, color="#444455", linewidth=0.7, linestyle="--", zorder=1)
    ax.text(1985, y + 30, lbl, color="#888899", fontsize=7, style="italic")

# Axes styling
ax.set_xlim(1985, 2038)
ax.set_ylim(0, 6500)
ax.set_xlabel("Estimated IOC / Delivery Year", color="#cccccc", fontsize=11)
ax.set_ylabel("Range (km)", color="#cccccc", fontsize=11)
ax.set_title("NATO DPS Capability Map — Programme Range vs. Delivery Year\n(Red bands = identified range-capability gaps)",
             color="white", fontsize=13, pad=14)
ax.tick_params(colors="#aaaaaa")
for spine in ax.spines.values():
    spine.set_edgecolor("#333344")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}"))

# Legend
legend_handles = [
    mpatches.Patch(color=color_map["Active"],       label="Active / In Service"),
    mpatches.Patch(color=color_map["In Dev"],        label="In Development / Procurement"),
    mpatches.Patch(color=color_map["Aspirational"],  label="Aspirational (target 2035)"),
    mpatches.Patch(color="#ff4444", alpha=0.4,       label="Identified Capability Gap"),
]
ax.legend(handles=legend_handles, loc="upper left",
          facecolor="#1a1a2e", edgecolor="#444455",
          labelcolor="white", fontsize=9)

plt.tight_layout()
plt.savefig("/home/user/Data_projects/dps_capability_gap_chart.png",
            dpi=160, bbox_inches="tight", facecolor=fig.get_facecolor())
print("Saved.")
