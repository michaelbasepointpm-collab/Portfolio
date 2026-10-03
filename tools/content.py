"""Portfolio content. Rendered into index.html by build2.py. No em dashes anywhere."""

# ------------------------------------------------------------------ Leasing route (head coordinator + REN)
ROUTE = [
    dict(
        key="sunrise", sketch="sunrise", n="01",
        role="Head leasing coordinator", kind="Upcoming lease-up",
        title="Sunrise Village: East &amp; West",
        address="2926 &amp; 2956 Venables St · Hastings-Sunrise",
        desc="146 new affordable homes in two Passive House buildings. Leasing starts December 2026 across three affordability tiers: shelter rate, rent-geared-to-income and low end of market, each with its own eligibility check.",
        roles=["Lease-up planning", "Marketing &amp; listings", "Income verification", "Applicant screening"],
        facts=[("Homes", "146"), ("Unit mix", "Studio to 3 bed"), ("Leasing from", "Dec 2026")],
        hood="Hastings-Sunrise", hood_sub="East Vancouver · Opening 2027",
        media=dict(kind="Rendering", base="sunrise-village-rendering", w=1200, h=675,
                   alt="Architectural rendering of Sunrise Village, two six-storey buildings around a landscaped courtyard"),
    ),
    dict(
        key="timbre", sketch="timbre-harmony", n="02",
        role="Head leasing coordinator", kind="Non-profit affordable",
        title="Timbre &amp; Harmony",
        address="1425 &amp; 1451 E 12th Ave · Grandview-Woodland",
        desc="Two Passive House buildings with 157 studio and one-bedroom homes: rent-geared-to-income homes for eligible seniors 55+, alongside low-end-of-market homes with no age restriction.",
        roles=["Showings", "Applicant screening", "Income verification", "Move-ins"],
        facts=[("Homes", "157"), ("Buildings", "2 × 6 storeys"), ("Opened", "2024")],
        hood="Grandview-Woodland", hood_sub="East 12th Ave · Opened 2024",
        media=dict(kind="Photo", base="timbre-harmony", w=1200, h=900,
                   alt="Aerial photo of Timbre and Harmony, two white six-storey buildings on East 12th Avenue"),
    ),
    dict(
        key="hawthorn", sketch="hawthorn", n="03",
        role="Head leasing coordinator", kind="Non-profit affordable",
        title="The Hawthorn",
        address="8705 French St · Marpole",
        desc="A six-storey Passive House building with 100 homes from studios to three bedrooms, mostly at low-end-of-market rents, with a common room and outdoor play area for families.",
        roles=["Marketing &amp; listings", "Showings", "Applicant screening", "Lease documentation"],
        facts=[("Homes", "100"), ("Unit mix", "Studio to 3 bed"), ("Opened", "2024")],
        hood="Marpole", hood_sub="South Vancouver · Opened 2024",
        media=dict(kind="Photo", base="the-hawthorn", w=1200, h=800,
                   alt="Photo of The Hawthorn, a six-storey rental building on a tree-lined corner in Marpole"),
    ),
    dict(
        key="alma", sketch="alma", n="04",
        role="Head leasing coordinator", kind="Furnished rentals",
        title="ALMA Gastown",
        address="455 Abbott St · Gastown",
        desc="A historic Gastown property adapted into 109 furnished rental suites, with shared fitness, bike storage and social space for residents.",
        roles=["Marketing &amp; listings", "Lead management", "Showings", "Move-ins"],
        facts=[("Suites", "109"), ("Storeys", "6"), ("Style", "Furnished")],
        hood="Gastown", hood_sub="Abbott &amp; Pender · Historic property",
        media=dict(kind="Photo", base="alma-455-abbott", w=1200, h=800,
                   alt="Photo of ALMA, a six-storey historic brick building at Abbott and West Pender Streets in Gastown"),
    ),
    # REN is filled in from research (see REN_DATA below)
]

REN_DATA = dict(
    key="ren", sketch="ren", n="05",
    role="Leasing agent", kind="New market rental",
    title="REN",
    address="5510 Joyce St · Renfrew-Collingwood",
    desc="A new 80-home secured market rental by Hudson Projects, completed in 2025, with a rooftop terrace, dog run, fitness centre and bike workshop.",
    roles=["Showings", "Lead management", "Applicant screening", "Move-ins"],
    facts=[("Homes", "80"), ("Storeys", "6"), ("Completed", "2025")],
    hood="Renfrew-Collingwood", hood_sub="Joyce St · Completed 2025",
    media=dict(kind="Rendering", base="ren-rendering", w=1200, h=750,
               alt="Architectural rendering of REN, a six-storey brick rental building with a curved corner and ground-floor shops"),
)

# ------------------------------------------------------------------ Multifamily (Basepoint), grouped by area
MULTIFAMILY = [
    dict(key="wynne", sketch="wynne", title="Wynne Manor", subtitle="1309 W 14th Ave",
         hood="Fairview · South Granville",
         desc="A 23-home, three-storey rental between Birch and Hemlock, close to parks and schools.",
         facts=[("Homes", "23"), ("Storeys", "3"), ("Built", "1959")]),
    dict(key="kaleden", sketch="kaleden", title="Kaleden", subtitle="1015 W 13th Ave",
         hood="Fairview",
         desc="Eleven one- and two-bedroom homes in a three-storey building from 1949.",
         facts=[("Homes", "11"), ("Storeys", "3"), ("Built", "1949")]),
    dict(key="hillcrest", sketch="hillcrest-mf", title="Hillcrest Manor", subtitle="3850 Cambie St",
         hood="Riley Park · Cambie Village",
         desc="Fourteen rental homes in a landscaped 1945 building near Queen Elizabeth Park.",
         facts=[("Homes", "14"), ("Unit mix", "Studio to 2 bed"), ("Built", "1945")]),
    dict(key="selkirk", sketch="selkirk", title="Selkirk", subtitle="8687 Selkirk St",
         hood="Marpole",
         desc="One- and two-bedroom homes in a 1957 building, substantially renovated in 2018.",
         facts=[("Unit mix", "1 &amp; 2 bed"), ("Built", "1957"), ("Renovated", "2018")]),
    dict(key="w71", sketch="w71", title="911 W 71st Ave", subtitle="",
         hood="Marpole",
         desc="Seven homes in a three-storey wood-frame building with a stucco façade.",
         facts=[("Homes", "7"), ("Storeys", "3"), ("Construction", "Wood frame")]),
    dict(key="seaview", sketch="seaview", title="Sea View Apartments", subtitle="2236 Trinity St",
         hood="Grandview-Woodland",
         desc="Ten one- and two-bedroom rental homes a few blocks from the waterfront.",
         facts=[("Homes", "10"), ("Unit mix", "1 &amp; 2 bed"), ("Built", "1961")]),
]

# ------------------------------------------------------------------ Strata examples
STRATA = [
    dict(key="hudson", sketch="hudson", title="The Hudson", address="610 Granville St · Downtown",
         desc="A single suite in a downtown condo tower behind restored heritage façades on Granville Street.",
         facts=[("Type", "Strata condo"), ("Scope", "Single suite")]),
    dict(key="independent", sketch="independent", title="The Independent", address="2508 Watson St · Mount Pleasant",
         desc="A single suite in a 21-storey Mount Pleasant tower near Main Street, completed in 2019.",
         facts=[("Type", "Strata condo"), ("Scope", "Single suite")]),
]

# ------------------------------------------------------------------ Licence switch
# Set to True once the BCFSA rental property management licence is issued, then rebuild.
LICENSED = False

CURRENT_TITLE = "Leasing Agent &amp; Property Manager Assistant"
CURRENT_TITLE_LICENSED = "Licensed Rental Property Manager"

BROKERAGE_TEXT = ("Currently with Basepoint Real Estate Group Corp., a licensed rental property management "
                  "brokerage in British Columbia. My leasing work is supported by Basepoint's property "
                  "management and administrative teams.")
BROKERAGE_TEXT_LICENSED = ("Licensed rental property manager in British Columbia. Leasing and rental property "
                           "management services are provided through Basepoint Real Estate Group Corp., a "
                           "licensed brokerage regulated by the BC Financial Services Authority.")


# ------------------------------------------------------------------ West End rentals (Forth Gen Holdings, contract)
WEST_END = [
    dict(key="bayside", sketch="we-bayside", title="Bayside Towers", address="1846 Nelson St", facts="43 homes · Built 1964"),
    dict(key="braeview", sketch="we-braeview", title="Braeview Manor", address="1260 Bidwell St", facts="76 homes · Built 1964"),
    dict(key="elliot", sketch="we-elliot", title="Elliot Towers", address="1350 Broughton St", facts="40 homes · Built 1963"),
    dict(key="heather", sketch="we-heather", title="Heather House", address="1650 Burnaby St", facts="95 homes · Built 1966"),
    dict(key="kevin", sketch="we-kevin", title="Kevin Manor", address="1661 Burnaby St", facts="64 homes · Built 1962"),
    dict(key="rosewoods", sketch="we-rosewoods", title="Rosewoods", address="1730 Pendrell St", facts="60 homes · Built 1979"),
]

# ------------------------------------------------------------------ Experience (real estate only)
JOBS = [
    dict(when="Sep 2025 to present", role="Leasing Agent &amp; Property Manager Assistant",
         org="Basepoint Real Estate Group · Vancouver",
         text="Head leasing coordinator for four rental communities, including the Sunrise Village lease-up starting December 2026. In charge of the multifamily rental portfolio and of strata leasing downtown and along Main Street, with weekly leasing reports for owners."),
    dict(when="May 2025 to Jul 2026", role="Concierge &amp; Building Manager Assistant",
         org="Lion's Gate Building Maintenance · Vancouver",
         text="Building operations at Vancouver House, Tesoro, Marquee and Lumina, working with Tribe Management and AWM: move-ins and move-outs, Form K and strata documentation, council minutes and vendor coordination. Front-line resident service with 95% resident satisfaction."),
    dict(when="Dec 2024 to Apr 2025", role="Digital Marketing &amp; Client Relations Specialist (contract)",
         org="Forth Gen Holdings Ltd · West End, Vancouver",
         text="Leasing across Forth Gen's West End rental portfolio: apartment tours, listings, virtual tours and marketplace advertising. Supported prospective and current tenants through furnished and winter rentals, contributing to more than $50K in winter rental revenue."),
]

BUILDING_GROUPS = [
    dict(label="Lease-ups", buildings=["Sunrise Village", "Timbre &amp; Harmony", "The Hawthorn", "ALMA Gastown", "REN"]),
    dict(label="Multifamily", buildings=["Wynne Manor", "Kaleden", "Hillcrest Manor", "Selkirk", "911 W 71st Ave", "Sea View Apartments"]),
    dict(label="Strata suites", buildings=["The Hudson", "The Independent"]),
    dict(label="West End rentals", buildings=["Bayside Towers", "Braeview Manor", "Elliot Towers", "Heather House", "Kevin Manor", "Rosewoods"]),
    dict(label="Building operations", buildings=["Vancouver House", "Tesoro", "Marquee", "Lumina"]),
]
