"""
Shared Industry Data — Single Source of Truth

Used by both the Solutions overview grid and each industry's detail
page, so the two never drift out of sync.
"""

INDUSTRIES = {
    "financial-services": {
        "n": "01",
        "title": "Financial Services",
        "href": "/solutions-financial-services",
        "desc": (
            "Automate KYC-heavy discovery, architect compliant hybrid-cloud "
            "solutions, and generate audit-ready proposals for regulated "
            "banking and capital markets deals."
        ),
        "points": [
            {
                "title": "Regulatory-Aware Discovery",
                "desc": (
                    "Opportunity intelligence flags data-residency, KYC, and "
                    "audit requirements early, so architecture decisions "
                    "aren't reworked after legal review."
                ),
            },
            {
                "title": "Hybrid-Cloud by Default",
                "desc": (
                    "Architecture recommendations account for on-premise "
                    "core banking systems that can't move to public cloud, "
                    "alongside the workloads that can."
                ),
            },
            {
                "title": "Audit-Ready Proposals",
                "desc": (
                    "Every generated solution package includes the "
                    "documentation trail compliance and procurement teams "
                    "expect to see before sign-off."
                ),
            },
        ],
        "deal_shape": (
            "Typically longer sales cycles with heavy involvement from "
            "compliance, security, and procurement &mdash; SixStage's "
            "architecture and RFP stages are built to keep pace with that "
            "review process instead of racing ahead of it."
        ),
    },
    "healthcare": {
        "n": "02",
        "title": "Healthcare &amp; Life Sciences",
        "href": "/solutions-healthcare",
        "desc": (
            "Navigate HIPAA and data-residency constraints automatically "
            "while designing architectures for clinical, research, and "
            "patient-data workloads."
        ),
        "points": [
            {
                "title": "HIPAA-Aware by Design",
                "desc": (
                    "Solution architecture flags PHI handling requirements "
                    "and recommends patterns that keep patient data within "
                    "compliant boundaries."
                ),
            },
            {
                "title": "Clinical vs. Research Workloads",
                "desc": (
                    "Distinguishes between production clinical systems and "
                    "research/analytics workloads, which often carry "
                    "different compliance and latency requirements."
                ),
            },
            {
                "title": "Vendor & Integration Mapping",
                "desc": (
                    "Accounts for the EHR and lab-system integrations that "
                    "typically dominate technical scope in healthcare deals."
                ),
            },
        ],
        "deal_shape": (
            "Deals often involve both IT and clinical stakeholders with "
            "different priorities &mdash; the generated solution package "
            "is written to be legible to both audiences."
        ),
    },
    "manufacturing": {
        "n": "03",
        "title": "Manufacturing &amp; Supply Chain",
        "href": "/solutions-manufacturing",
        "desc": (
            "Plan automation projects across OT and IT boundaries &mdash; "
            "from plant-floor integration to end-to-end supply chain "
            "visibility."
        ),
        "points": [
            {
                "title": "OT/IT Boundary Awareness",
                "desc": (
                    "Architecture recommendations distinguish operational "
                    "technology (plant floor, SCADA) from IT systems, since "
                    "the two have very different change-management rules."
                ),
            },
            {
                "title": "Supply Chain Visibility Focus",
                "desc": (
                    "Opportunity intelligence weighs end-to-end visibility "
                    "and traceability requirements common in multi-tier "
                    "supply chains."
                ),
            },
            {
                "title": "Legacy System Integration",
                "desc": (
                    "Accounts for the reality that plant-floor systems are "
                    "often decades old and not going anywhere soon."
                ),
            },
        ],
        "deal_shape": (
            "Projects frequently span multiple sites and business units "
            "&mdash; the POC builder stage scopes a pilot narrow enough to "
            "prove value before asking for a multi-site rollout."
        ),
    },
    "public-sector": {
        "n": "04",
        "title": "Public Sector",
        "href": "/solutions-public-sector",
        "desc": (
            "Meet procurement and security accreditation requirements from "
            "the first discovery call, with architecture recommendations "
            "built for government compliance frameworks."
        ),
        "points": [
            {
                "title": "Procurement-Ready From Discovery",
                "desc": (
                    "Opportunity intelligence surfaces the procurement "
                    "vehicle and accreditation requirements early, before "
                    "they become late-stage blockers."
                ),
            },
            {
                "title": "Compliance Framework Fit",
                "desc": (
                    "Architecture recommendations are scoped against "
                    "relevant government security and compliance "
                    "frameworks, not just generic cloud best practices."
                ),
            },
            {
                "title": "Long-Cycle-Friendly Documentation",
                "desc": (
                    "Generated packages hold up over the longer review and "
                    "approval timelines typical of public-sector "
                    "procurement."
                ),
            },
        ],
        "deal_shape": (
            "Sales cycles are long and formal &mdash; SixStage's output is "
            "meant to survive being re-read by a review board months after "
            "it was generated."
        ),
    },
    "insurance": {
        "n": "05",
        "title": "Insurance",
        "href": "/solutions-insurance",
        "desc": (
            "Accelerate claims and underwriting automation opportunities "
            "with POC plans scoped around measurable loss-ratio and "
            "cycle-time outcomes."
        ),
        "points": [
            {
                "title": "Claims & Underwriting Focus",
                "desc": (
                    "Opportunity intelligence is tuned to recognize the "
                    "process-automation patterns most common in claims and "
                    "underwriting workflows."
                ),
            },
            {
                "title": "Outcome-Scoped POCs",
                "desc": (
                    "POC plans are built around measurable outcomes &mdash; "
                    "cycle-time reduction, loss-ratio impact &mdash; instead "
                    "of open-ended technical exploration."
                ),
            },
            {
                "title": "Regulated-Data Handling",
                "desc": (
                    "Architecture recommendations account for the "
                    "policyholder and claims data sensitivity typical of "
                    "insurance workloads."
                ),
            },
        ],
        "deal_shape": (
            "Buyers want to see the business case, not just the "
            "architecture &mdash; the generated package leads with the "
            "measurable outcome the POC is scoped to prove."
        ),
    },
    "technology": {
        "n": "06",
        "title": "Technology &amp; SaaS",
        "href": "/solutions-technology",
        "desc": (
            "Scope integrations and multi-tenant architecture for platform "
            "and infrastructure deals, from proof-of-concept to production "
            "rollout."
        ),
        "points": [
            {
                "title": "Multi-Tenant Architecture Fit",
                "desc": (
                    "Architecture recommendations default to multi-tenant "
                    "patterns when the buyer is themselves building a "
                    "platform product, not a single internal system."
                ),
            },
            {
                "title": "Integration-Heavy Scoping",
                "desc": (
                    "Opportunity intelligence weighs API and integration "
                    "surface area, usually the largest source of technical "
                    "risk in platform and infrastructure deals."
                ),
            },
            {
                "title": "POC to Production Path",
                "desc": (
                    "POC plans are built with an explicit path to "
                    "production rollout, not as a standalone proof that "
                    "dead-ends after the pilot."
                ),
            },
        ],
        "deal_shape": (
            "Technical buyers evaluate quickly and expect precision "
            "&mdash; the generated architecture is detailed enough to "
            "survive scrutiny from an engineering team, not just a "
            "business stakeholder."
        ),
    },
}
