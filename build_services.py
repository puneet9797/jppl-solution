import os

# Data structure containing information for all 24 services
services_data = [
    # Category A: Business Setup & Registration Services
    {
        "category": "Business Setup & Registration Services",
        "cat_slug": "legal",
        "name": "GST Registration Service",
        "slug": "gst-registration",
        "icon": "fa-scale-balanced",
        "image": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=800&q=80",
        "tagline": "We prepare, review, and successfully file your GST application for fast approval.",
        "overview": "We handle complete end-to-end registration for proprietorships, partnerships, LLPs, Private Limited companies, One Person Companies (OPC), and e-commerce sellers. We prepare, review, and successfully file your GST application for fast approval.",
        "value": "Grants your business a formal legal identity, unlocks Input Tax Credit (ITC), allows cross-border pan-India commerce, and qualifies your firm for prestigious Government Tenders and GeM registrations.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "PAN Card, Aadhaar Card, Business Address Proof (Rent Agreement or Utility Bill), Photo, and Bank Details.",
        "related": ["msme-udyam-registration", "fssai-food-license", "trademark-registration"]
    },
    {
        "category": "Business Setup & Registration Services",
        "cat_slug": "legal",
        "name": "MSME / Udyam Registration Service",
        "slug": "msme-udyam-registration",
        "icon": "fa-briefcase",
        "image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80",
        "tagline": "We secure your official government enterprise recognition within 24 hours.",
        "overview": "We execute your MSME application to secure your official government enterprise recognition within 24 hours. We align your business with Ministry of MSME benefits and verify priority sector features.",
        "value": "Unlocks massive government subsidy benefits, lower interest rates on business bank loans, priority sector lending, collateral-free credit access, and faster processing of industrial approvals.",
        "checklist_type": "Processing Timeline",
        "checklist_content": "Guaranteed 1-Day processing and certificate delivery from final submission.",
        "related": ["gst-registration", "fssai-food-license", "startup-india-recognition"]
    },
    {
        "category": "Business Setup & Registration Services",
        "cat_slug": "legal",
        "name": "FSSAI Licensing Service",
        "slug": "fssai-food-license",
        "icon": "fa-utensils",
        "image": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&w=800&q=80",
        "tagline": "We handle the complete documentation and mapping required to secure your food business license.",
        "overview": "We handle the complete documentation and mapping required to secure your FSSAI food business license. We submit food safety dossiers and align approvals for restaurants, hotels, cloud kitchens, grocery traders, and food processors.",
        "value": "Establishes complete legal compliance, builds consumer confidence in quality, avoids heavy municipal closures/penalties, and is strictly required to onboard onto online delivery platforms (Zomato/Swiggy).",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "Business address proof, identity proof, list of food categories, and layout map of the manufacturing site (for manufacturing licenses).",
        "related": ["gst-registration", "trade-licence", "factory-licence"]
    },
    {
        "category": "Business Setup & Registration Services",
        "cat_slug": "legal",
        "name": "IEC Import Export Service",
        "slug": "iec-import-export-code",
        "icon": "fa-plane-departure",
        "image": "https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=800&q=80",
        "tagline": "We execute your DGFT applications to obtain your 10-digit Import Export Code.",
        "overview": "We compile and execute your DGFT applications to obtain your 10-digit Import Export Code. We ensure cross-border shipping compliance and setup pan-India export privileges.",
        "value": "Grants your business global marketplace access, enables seamless import/export shipments, and allows your firm to claim attractive government export incentive schemes.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "PAN Card of the entity, bank certificate or canceled check, address proof of business.",
        "related": ["gst-registration", "trademark-registration", "iso-certification"]
    },
    {
        "category": "Business Setup & Registration Services",
        "cat_slug": "legal",
        "name": "Trademark Registration Service",
        "slug": "trademark-registration",
        "icon": "fa-registered",
        "image": "https://images.unsplash.com/photo-1606857521015-7f9fcf423740?auto=format&fit=crop&w=800&q=80",
        "tagline": "We lock down and legally protect your unique brand name, logo, and identity.",
        "overview": "We lock down and legally protect your unique brand name, logo, design symbols, and corporate taglines. We handle filing, database classification search, and final registration tracking under the Trademarks Act.",
        "value": "Delivers exclusive legal ownership, prevents copycats from diluting your market reputation, and builds valuable intangible business equity over its 10-year renewable validity.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "Logo/brand name copy, identity proof of applicant, Power of Attorney authorization document.",
        "related": ["gst-registration", "iec-import-export-code", "startup-india-recognition"]
    },
    
    # Category B: Compliance & Industrial Licensing
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "ISO Certification Service",
        "slug": "iso-certification",
        "icon": "fa-certificate",
        "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=800&q=80",
        "tagline": "We secure globally recognized quality management standards for your business.",
        "overview": "We handle the complete ISO registration and audit preparation process for internationally recognized quality standards (such as ISO 9001 for quality, ISO 14001 for environment, and ISO 27001 for security) to verify your firm's compliance.",
        "value": "Maximizes your business reputation, validates operational efficiency and safety to global consumers, and satisfies core eligibility criteria for large-scale corporate and government bids.",
        "checklist_type": "Required Audit Documents",
        "checklist_content": "Business registration copy, scope of work description, standard operating procedures checklist, and brief organizational chart.",
        "related": ["zed-green-certification", "bis-standards-certification", "gem-portal-registration"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "ZED Certification Service",
        "slug": "zed-green-certification",
        "icon": "fa-leaf",
        "image": "https://images.unsplash.com/photo-1506084868230-bb9d95c24759?auto=format&fit=crop&w=800&q=80",
        "tagline": "We deploy specialized green manufacturing certification frameworks.",
        "overview": "We manage your ZED certification application under the Ministry of MSME framework. We audit, compile documentation, and verify your zero-defect manufacturing parameters to reduce waste and secure priority subsidies.",
        "value": "Dramatically improves factory productivity, minimizes manufacturing defects, and provides priority access to specific government credit incentives, clean energy grants, and concession rates.",
        "checklist_type": "Statutory Eligibility",
        "checklist_content": "Available only to MSMEs with a valid Udyam Registration engaged in active manufacturing operations.",
        "related": ["msme-udyam-registration", "iso-certification", "factory-licence"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "GeM Portal Registration Service",
        "slug": "gem-portal-registration",
        "icon": "fa-cart-shopping",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "tagline": "We register and map your products on the central government procurement portal.",
        "overview": "We execute direct registration and product catalog mapping to list your company's offerings on India's centralized public procurement portal. We handle seller credentials, catalog setup, and brand approvals.",
        "value": "Opens the door to secure direct, paperless government purchase orders, participate in transparent public bidding, and access highly predictable government payment cycles.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "PAN, Aadhaar, GST Certificate, Bank Account Details, and active Udyam Certificate (if applicable).",
        "related": ["gst-registration", "msme-udyam-registration", "government-tender-consultancy"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "BIS Certification Service",
        "slug": "bis-standards-certification",
        "icon": "fa-award",
        "image": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=800&q=80",
        "tagline": "We coordinate product conformity and safety standard testing.",
        "overview": "We handle the entire BIS registration process, coordinating lab test approvals, safety inspections, and Bureau of Indian Standards compliance mapping.",
        "value": "Guarantees raw material and product safety, mandates regulatory compliance for manufacturing market entry in India, and builds concrete consumer confidence.",
        "checklist_type": "Audit & Lab Testing",
        "checklist_content": "Requires factory raw-material inspection, sample collections, and laboratory testing at BIS recognized labs.",
        "related": ["iso-certification", "zed-green-certification", "factory-licence"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "Trade License Service",
        "slug": "trade-licence",
        "icon": "fa-house-medical",
        "image": "https://images.unsplash.com/photo-1534452203293-494d7ddbf7e0?auto=format&fit=crop&w=800&q=80",
        "tagline": "We secure municipal operating licenses for your business.",
        "overview": "We prepare and submit municipal corporation applications to secure your commercial trade license. We coordinate land bylaws, rent agreements, and local municipal compliance filings.",
        "value": "Ensures your day-to-day operations align with local municipal bylaws, helping your business avoid unexpected administrative closures, closures due to zoning, or legal penalties.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "Sanction layout plan, property tax receipt, municipal occupancy certificate, lease agreement, and NOC from immediate neighbors.",
        "related": ["factory-licence", "gst-registration", "fssai-food-license"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "Factory License Service",
        "slug": "factory-licence",
        "icon": "fa-industry",
        "image": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80",
        "tagline": "We secure industrial plan approvals and safety registrations.",
        "overview": "We execute safety registrations and factory plan approvals under the Factories Act. We compile structure certificates, pollution control filings, machinery specs, and fire NOCs.",
        "value": "Protects worker safety, satisfies labor law compliance parameters, and secures clean governmental approval to operate machinery and layout plans.",
        "checklist_type": "Required Approvals",
        "checklist_content": "Requires prior Factory Plan approval, NOC from Pollution Control Board, Fire Safety NOC, and stability certificate of the building structure.",
        "related": ["trade-licence", "bis-standards-certification", "zed-green-certification"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "Solar Energy Service",
        "slug": "solar-energy-service",
        "icon": "fa-sun",
        "image": "https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=800&q=80",
        "tagline": "We coordinate solar net metering approvals, government subsidy claims, and plant setups.",
        "overview": "We manage the end-to-end solar setup process for industrial, commercial, and residential clients. This includes site feasibility assessments, net metering approval filings with local Discoms, and processing central solar subsidies (including PM Surya Ghar applications) to ensure high-efficiency power integration.",
        "value": "Secures up to 90% reduction in electricity bills, ensures seamless net metering billing approvals to sell excess energy, processes attractive capital subsidies, and boosts your corporate environmental compliance (ESG) profiles.",
        "checklist_type": "Required Setup Checklist",
        "checklist_content": "Latest electricity bill copy, roof ownership proof or NOC, Aadhaar & PAN card of the applicant, and site photographs.",
        "related": ["zed-green-certification", "factory-licence", "iso-certification"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "EPR Battery Waste Management Registration",
        "slug": "epr-battery-registration",
        "icon": "fa-car-battery",
        "image": "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=800&q=80",
        "tagline": "We secure CPCB EPR registration and manage battery waste compliance.",
        "overview": "We manage the complete registration and compliance process on the centralized Central Pollution Control Board (CPCB) portal for battery manufacturers, importers, recyclers, and refurbishers under the Battery Waste Management Rules, 2022.",
        "value": "Avoids heavy statutory penalties, fulfills mandatory collection and recycling targets, and enables the generation/trading of EPR certificates to secure legal manufacturing and import authorization.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "GST Certificate, PAN Card, IEC (Import Export Code, if importing), Battery chemistry/weight specifications, and recycler partner agreement.",
        "related": ["iec-import-export-code", "factory-licence", "iso-certification"]
    },
    {
        "category": "Compliance & Industrial Licensing",
        "cat_slug": "quality",
        "name": "EPR Waste Tyre Management Registration",
        "slug": "epr-tyre-registration",
        "icon": "fa-recycle",
        "image": "https://images.unsplash.com/photo-1578844251758-2f71da64c96f?auto=format&fit=crop&w=800&q=80",
        "tagline": "We file and execute CPCB tyre EPR registration and annual compliance.",
        "overview": "We handle end-to-end registration and return filings on the CPCB EPR Portal for tyre producers, importers, and recyclers under the Hazardous and Other Wastes Amendment Rules, 2022.",
        "value": "Satisfies mandatory annual tyre recycling targets, facilitates seamless purchase and transfer of tyre EPR certificates, and ensures total operational compliance for tyre importers and manufacturers.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "GST Certificate, PAN Card of the company, IEC (for importers), technical specifications of tyres (weight, type), and authorized recycler agreements.",
        "related": ["iec-import-export-code", "factory-licence", "zed-green-certification"]
    },
    
    # Category C: Bidding & Capital Projects
    {
        "category": "Bidding & Capital Projects",
        "cat_slug": "capital",
        "name": "Government Tender Submission Service",
        "slug": "government-tender-consultancy",
        "icon": "fa-file-invoice-dollar",
        "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80",
        "tagline": "We research open bids, compile technical portfolios, and submit your digital bids.",
        "overview": "We research open bids, compile exact technical portfolios, and execute your final digital bid submissions on state and national public procurement portals. We manage Digital Signature Certificates (DSC) and clarify bids.",
        "value": "Includes exhaustive tender searching, precision documentation compilation, technical bid optimization, and financial bid submission strategies to dramatically scale your bid success rate.",
        "checklist_type": "Submission Layout",
        "checklist_content": "Includes Tender Search, Bid Preparation, Class 3 Digital Signature Setup, Technical Query Submissions, and Financial Bidding Strategy.",
        "related": ["gem-portal-registration", "dpr-project-report-preparation", "iso-certification"]
    },
    {
        "category": "Bidding & Capital Projects",
        "cat_slug": "capital",
        "name": "DPR / Project Report Preparation Service",
        "slug": "dpr-project-report-preparation",
        "icon": "fa-file-circle-check",
        "image": "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=800&q=80",
        "tagline": "We engineer bank-grade Detailed Project Reports and CMA calculations.",
        "overview": "We engineer detailed, accurate bank-grade Detailed Project Reports (DPR), MSME industrial project profiles, and comprehensive CMA data sheets to secure your bank loans and subsidy grants.",
        "value": "Perfect for optimizing commercial bank loan approvals, creating bulletproof investor presentations, and securing capital under government credit-linked subsidy schemes.",
        "checklist_type": "Report Deliverables",
        "checklist_content": "Includes Market Feasibility analysis, Financial Model forecasts (5-10 years), Balance Sheet projection sheets, CMA Data files, and Cash Flow calculations.",
        "related": ["financial-advisory-services", "government-tender-consultancy", "startup-india-recognition"]
    },
    {
        "category": "Bidding & Capital Projects",
        "cat_slug": "capital",
        "name": "Startup India Recognition Service",
        "slug": "startup-india-recognition",
        "icon": "fa-rocket",
        "image": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=800&q=80",
        "tagline": "We file and secure your premium DPIIT startup accreditation.",
        "overview": "We execute your DPIIT startup application to secure Startup India recognition. We structure your scale narrative, prepare innovation briefs, and verify multi-year tax exemptions.",
        "value": "Open to innovative business models (under 10 years old with turnover under 100 Crore), offering multi-year tax exemptions, fast-tracked patent filings, self-compliance benefits, and access to government venture funds.",
        "checklist_type": "Eligibility Criteria",
        "checklist_content": "Must be incorporated as a Private Limited, LLP, or registered Partnership. Must show innovation, scalability, and product development potential.",
        "related": ["msme-udyam-registration", "trademark-registration", "dpr-project-report-preparation"]
    },
    
    # Category D: IT Services
    {
        "category": "IT Services",
        "cat_slug": "digital",
        "name": "Custom Software & App Development",
        "slug": "custom-software-app-development",
        "icon": "fa-mobile-screen-button",
        "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80",
        "tagline": "We engineer tailored custom software architectures and premium iOS & Android mobile applications.",
        "overview": "We design, build, and deploy native and cross-platform mobile apps, cloud-native custom software platforms, and digital products tailored to your corporate operations.",
        "value": "Accelerates business automation, enhances user engagement through sleek application frontends, and scales backend infrastructures using modern technologies.",
        "checklist_type": "Deployment Model",
        "checklist_content": "Includes UX/UI wireframing, native iOS (Swift) & Android (Kotlin) development, API integration, and play/app store compliance submissions.",
        "related": ["website-development-services", "erp-crm-solutions", "cloud-cybersecurity-services"]
    },
    {
        "category": "IT Services",
        "cat_slug": "digital",
        "name": "Custom ERP & CRM Solutions",
        "slug": "erp-crm-solutions",
        "icon": "fa-network-wired",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80",
        "tagline": "We deliver customized ERP and CRM software to integrate your corporate workflows.",
        "overview": "We engineer business management portals, inventory modules, lead funnels, and CRM pipelines to align your production, sales, and accounts under one dashboard.",
        "value": "Optimizes working capital tracking, minimizes manual data redundancy, enhances client retention tracking, and secures enterprise resource auditing.",
        "checklist_type": "Standard Features",
        "checklist_content": "Role-based access controls, automatic invoice logging, lead stage pipelines, inventory alerts, and WhatsApp/Email API integrations.",
        "related": ["custom-software-app-development", "website-development-services", "financial-advisory-services"]
    },
    {
        "category": "IT Services",
        "cat_slug": "digital",
        "name": "Cloud Services & Cyber Security",
        "slug": "cloud-cybersecurity-services",
        "icon": "fa-shield-halved",
        "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=800&q=80",
        "tagline": "We build secure cloud architectures and execute compliance cybersecurity audits.",
        "overview": "We configure secure Amazon Web Services (AWS) or Microsoft Azure clouds, deploy secure firewalls, and perform systematic vulnerability assessments to safeguard client data.",
        "value": "Guarantees 99.9% application uptime, protects corporate networks from ransomware attacks, and helps secure institutional data-privacy compliance.",
        "checklist_type": "Audit Protocols",
        "checklist_content": "Vulnerability Assessment and Penetration Testing (VAPT), AWS/Azure IAM setups, firewalls config, and automated disaster recovery backups.",
        "related": ["custom-software-app-development", "erp-crm-solutions", "iso-certification"]
    },
    {
        "category": "IT Services",
        "cat_slug": "digital",
        "name": "Website Development Service",
        "slug": "website-development-services",
        "icon": "fa-laptop-code",
        "image": "https://images.unsplash.com/photo-1547082299-de196ea013d6?auto=format&fit=crop&w=800&q=80",
        "tagline": "We engineer custom, responsive, fast-loading corporate digital real estate.",
        "overview": "We engineer custom, responsive, fast-loading corporate digital real estate. We manage domain registration, web hosting, SSL setups, Google My Business (GMB) configurations, and professional business emails.",
        "value": "Optimizes your business visibility with fast-loading, SEO-friendly architectures, professional business email setups, and verified Google My Business (GMB) map pins.",
        "checklist_type": "Engineering Deliverables",
        "checklist_content": "Custom UI design mockup, clean HTML5/CSS/JS development, Domain & hosting setup, SSL security integration, and search engine registrations.",
        "related": ["digital-marketing-services", "trademark-registration", "startup-india-recognition"]
    },
    {
        "category": "IT Services",
        "cat_slug": "digital",
        "name": "Performance Digital Marketing Service",
        "slug": "digital-marketing-services",
        "icon": "fa-share-nodes",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "tagline": "We execute social media and search ads lead campaigns.",
        "overview": "We deploy and manage PPC ad campaigns across Facebook, Google, and LinkedIn. We target high-value buyers, setup tracking analytics, and manage consistent lead-generation pipelines.",
        "value": "Builds massive brand awareness, drives consistent lead-generation pipelines, and maximizes client retention through transparent measurable analytics.",
        "checklist_type": "Services Scope",
        "checklist_content": "Includes Social Media Management (SMM), Search Engine Optimization (SEO), PPC Ad Campaign runs, Content design, and analytics mapping.",
        "related": ["website-development-services", "financial-advisory-services", "trademark-registration"]
    },
    
    # Category E: Core Welfare & Healthcare Operations
    {
        "category": "Core Welfare & Healthcare Operations",
        "cat_slug": "specialized",
        "name": "Women Entrepreneur Framework Service",
        "slug": "women-entrepreneur-consultant",
        "icon": "fa-female",
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=800&q=80",
        "tagline": "We align funding and grants for female business leaders.",
        "overview": "We compile and execute applications for women-centric government funding, interest subsidies, and business grants under state and national development frameworks.",
        "value": "Empowers female leaders with industry networking circles, government grant support schemes (e.g., Mudra, Mahila Co-op), and customized industrial business training modules.",
        "checklist_type": "Specialized Support",
        "checklist_content": "Access to Mahila-centric bank schemes, specific interest subsidy lists, and direct startup advisory panels.",
        "related": ["msme-udyam-registration", "financial-advisory-services", "startup-india-recognition"]
    },
    {
        "category": "Core Welfare & Healthcare Operations",
        "cat_slug": "specialized",
        "name": "Financial Planning Service",
        "slug": "financial-advisory-services",
        "icon": "fa-chart-line",
        "image": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=800&q=80",
        "tagline": "We optimize assets, plan taxes, and structure cash flow pipelines.",
        "overview": "We structure corporate cash flow models, prepare tax optimization filings, and balance working capital pipelines to secure corporate operations.",
        "value": "Specializes in systematic wealth growth, legal tax optimization strategies, meticulous cash flow forecasting, and structured capital advisory for corporate expansions.",
        "checklist_type": "Core Solutions",
        "checklist_content": "Asset Allocation models, Corporate Tax advisory, Working Capital optimization, and Debt structure advisory.",
        "related": ["dpr-project-report-preparation", "women-entrepreneur-consultant", "healthcare-services"]
    },
    {
        "category": "Core Welfare & Healthcare Operations",
        "cat_slug": "specialized",
        "name": "Healthcare Operations Service",
        "slug": "healthcare-services",
        "icon": "fa-heartpulse",
        "image": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=800&q=80",
        "tagline": "We plan corporate wellness and setup medical safety blueprints.",
        "overview": "We execute corporate medical checkup scheduling, organize preventive immunization drives, and build health safety blueprints for employees.",
        "value": "Delivers complete medical safety blueprints, emergency planning protocols, and sustainable, long-term health programs for employee retention.",
        "checklist_type": "Advisory Scope",
        "checklist_content": "Corporate wellness packages, statutory compliance checklist for work safety, and emergency response training setups.",
        "related": ["lab-corp-services", "financial-advisory-services", "women-entrepreneur-consultant"]
    },
    {
        "category": "Core Welfare & Healthcare Operations",
        "cat_slug": "specialized",
        "name": "Lab Diagnostics Service",
        "slug": "lab-corp-services",
        "icon": "fa-flask-vial",
        "image": "https://images.unsplash.com/photo-1579165466521-35b8339ef7cd?auto=format&fit=crop&w=800&q=80",
        "tagline": "We coordinate NABL diagnostics test collections and medical reports.",
        "overview": "We coordinate diagnostic testing collections and deliver NABL/CAP compliant laboratory reports to your employees or family.",
        "value": "Offers frictionless sample home collection options, state-of-the-art technological precision, fast digital report turnarounds, and tailored wellness tracking databases.",
        "checklist_type": "Quality Specifications",
        "checklist_content": "Certified under NABL (National Accreditation Board for Testing and Calibration Laboratories) guidelines to assure report precision.",
        "related": ["healthcare-services", "financial-advisory-services", "women-entrepreneur-consultant"]
    },
    {
        "category": "Core Welfare & Healthcare Operations",
        "cat_slug": "specialized",
        "name": "Agriculture Business Service",
        "slug": "agriculture-business-services",
        "icon": "fa-seedling",
        "image": "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=800&q=80",
        "tagline": "We file APEDA registrations, organic certifications, and subsidy claims.",
        "overview": "We file APEDA export registrations, manage organic farming certification audits, verify soil reports, and secure government agriculture machinery subsidies.",
        "value": "Enables compliance for agro-export markets, unlocks state/central agricultural grants, assures quality with organic farming certifications, and assists in farm machinery/setup approvals.",
        "checklist_type": "Typical Document Requirements",
        "checklist_content": "Land ownership proof or lease agreement, FSSAI registration (for processed food), business registration certificate, applicant PAN & Aadhaar, and test reports of soil/produce if certifying organic.",
        "related": ["fssai-food-license", "iec-import-export-code", "msme-udyam-registration"]
    }
]

# Base template HTML code for services
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{service_name} | JPPL Digital Services</title>
    <meta name="description" content="{overview_brief}">
    <meta name="keywords" content="{meta_keywords}">
    <link rel="canonical" href="https://jioliteproducts.com/services/{slug}.html">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://jioliteproducts.com/services/{slug}.html">
    <meta property="og:title" content="{service_name} | JPPL Digital Services">
    <meta property="og:description" content="{overview_brief}">
    <meta property="og:image" content="https://jioliteproducts.com/assets/hero_banner.png">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://jioliteproducts.com/services/{slug}.html">
    <meta property="twitter:title" content="{service_name} | JPPL Digital Services">
    <meta property="twitter:description" content="{overview_brief}">
    <meta property="twitter:image" content="https://jioliteproducts.com/assets/hero_banner.png">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS (pointing up one folder level) -->
    <link rel="stylesheet" href="../styles.css">
</head>
<body class="service-detail-page">

    <!-- TOP CONTACT BAR -->
    <div class="top-bar" id="topBar">
        <div class="container top-bar-container">
            <div class="top-bar-contacts">
                <a href="tel:+919369288078" class="contact-link"><i class="fa-solid fa-phone phone-icon"></i> +91 9369288078</a>
                <span class="separator">|</span>
                <a href="mailto:jioliteproducts@gmail.com" class="contact-link"><i class="fa-solid fa-envelope envelope-icon"></i> jioliteproducts@gmail.com</a>
                <span class="separator">|</span>
                <span class="contact-link"><i class="fa-solid fa-location-dot location-icon"></i> Kanpur, Uttar Pradesh</span>
            </div>
            <div class="top-bar-cta">
                <a href="#quote-section" class="btn btn-gold btn-small animate-pulse">Enquire Now</a>
            </div>
        </div>
    </div>

    <!-- STICKY NAVBAR -->
    <header class="main-header" id="mainHeader">
        <div class="container nav-container">
            <a href="../index.html" class="logo-area" id="logoLink">
                <img src="../assets/logo.png" alt="JPPL Logo" class="logo-img">
            </a>

            <!-- Mobile Navigation Menu Toggle -->
            <button class="mobile-nav-toggle" id="mobileNavToggle" aria-label="Toggle navigation">
                <span class="hamburger"></span>
            </button>

            <!-- Navigation Links -->
            <nav class="nav-menu" id="navMenu">
                <ul class="nav-list">
                    <li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li>
                    <li class="nav-item"><a href="../about.html" class="nav-link">About Us</a></li>
                    
                    <!-- Mega Menu Dropdown -->
                    <li class="nav-item has-mega-menu">
                        <a href="../services.html" class="nav-link dropdown-trigger active">Services <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
                        <div class="mega-menu" id="megaMenu">
                            <div class="container mega-menu-grid">
                                <!-- Col 1: IT Services -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-laptop-code col-icon"></i> IT Services</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="custom-software-app-development.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Software & App Dev</a></li>
                                        <li><a href="erp-crm-solutions.html"><i class="fa-solid fa-chevron-right link-bullet"></i> ERP & CRM Portals</a></li>
                                        <li><a href="cloud-cybersecurity-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Cloud & Cyber Security</a></li>
                                        <li><a href="website-development-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Website Engineering</a></li>
                                        <li><a href="digital-marketing-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Digital Marketing</a></li>
                                    </ul>
                                </div>
                                <!-- Col 2: Business Setup & Registration Services -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-briefcase col-icon"></i> Legal Setup</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="gst-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> GST Registration Service</a></li>
                                        <li><a href="msme-udyam-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> MSME / Udyam Service</a></li>
                                        <li><a href="fssai-food-license.html"><i class="fa-solid fa-chevron-right link-bullet"></i> FSSAI Licensing Service</a></li>
                                        <li><a href="iec-import-export-code.html"><i class="fa-solid fa-chevron-right link-bullet"></i> IEC Import Export Service</a></li>
                                        <li><a href="trademark-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Trademark Registration Service</a></li>
                                    </ul>
                                </div>
                                <!-- Col 3: Compliance & Industrial Licensing -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-certificate col-icon"></i> Quality & Licensing</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="iso-certification.html"><i class="fa-solid fa-chevron-right link-bullet"></i> ISO Certification Service</a></li>
                                        <li><a href="zed-green-certification.html"><i class="fa-solid fa-chevron-right link-bullet"></i> ZED Certification Service</a></li>
                                        <li><a href="gem-portal-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> GeM Registration Service</a></li>
                                        <li><a href="bis-standards-certification.html"><i class="fa-solid fa-chevron-right link-bullet"></i> BIS Standards Service</a></li>
                                        <li><a href="trade-licence.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Trade License Service</a></li>
                                        <li><a href="factory-licence.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Factory License Service</a></li>
                                        <li><a href="solar-energy-service.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Solar Energy Service</a></li>
                                        <li><a href="epr-battery-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Battery EPR Service</a></li>
                                        <li><a href="epr-tyre-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Tyre EPR Service</a></li>
                                    </ul>
                                </div>
                                <!-- Col 4: Bidding & Capital Projects -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-landmark col-icon"></i> Capital Advisory</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="government-tender-consultancy.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Government Tender Submission</a></li>
                                        <li><a href="dpr-project-report-preparation.html"><i class="fa-solid fa-chevron-right link-bullet"></i> DPR & Bank Projects</a></li>
                                        <li><a href="startup-india-recognition.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Startup India Recognition</a></li>
                                    </ul>
                                </div>
                                <!-- Col 5: Core Welfare & Healthcare Operations -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-handshake col-icon"></i> Specialized Services</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="women-entrepreneur-consultant.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Women Mentorship</a></li>
                                        <li><a href="financial-advisory-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Financial Advisory</a></li>
                                        <li><a href="healthcare-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Corporate Health</a></li>
                                        <li><a href="lab-corp-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Lab Diagnostics (NABL)</a></li>
                                        <li><a href="agriculture-business-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Agriculture Services</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="nav-item"><a href="../services.html" class="nav-link">Services Hub</a></li>
                    <li class="nav-item"><a href="#quote-section" class="nav-link">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- SERVICE HERO BANNER -->
    <section class="page-title-section service-title-banner">
        <div class="container text-center">
            <span class="section-subtitle text-gold-accent">{category}</span>
            <h1 class="page-main-heading">{service_name}</h1>
            <p class="page-sub-heading">{tagline}</p>
        </div>
    </section>

    <!-- MAIN SERVICE DETAIL GRID -->
    <section class="service-detail-container">
        <div class="container detail-page-grid">
            
            <!-- LEFT COLUMN: CONTENT -->
            <main class="service-main-content">
                
                <!-- Illustrative Service Banner Image -->
                <div class="service-banner-image-wrapper scroll-fade" style="margin-bottom: 30px; border-radius: var(--border-radius); overflow: hidden; box-shadow: var(--color-card-shadow); height: 280px; border: 1px solid var(--color-border);">
                    <img src="{image}" alt="{service_name}" style="width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform var(--transition-normal);">
                </div>
                
                <!-- Overview -->
                <div class="content-card scroll-fade">
                    <h2 class="detail-section-title"><i class="fa-solid fa-info-circle section-title-icon"></i> Service Overview</h2>
                    <p class="content-text">{overview}</p>
                </div>

                <!-- Client Value & Statutory Benefits -->
                <div class="content-card scroll-fade">
                    <h2 class="detail-section-title"><i class="fa-solid fa-award section-title-icon"></i> Statutory Benefits & Business Value</h2>
                    <p class="content-text">{value}</p>
                </div>

                <!-- Checklist / Processing Timeline -->
                <div class="content-card scroll-fade">
                    <h2 class="detail-section-title"><i class="fa-solid fa-clipboard-list section-title-icon"></i> {checklist_type}</h2>
                    <p class="content-text checklist-text">{checklist_content}</p>
                </div>

                <!-- Related Services -->
                <div class="related-services-wrapper scroll-fade">
                    <h3 class="related-heading">Other Related Services</h3>
                    <div class="related-grid">
                        {related_links}
                    </div>
                </div>

            </main>

            <!-- RIGHT COLUMN: STICKY FORM -->
            <aside class="service-detail-sidebar">
                <div class="sidebar-sticky-wrapper">
                    <div class="hero-form-card" id="quickConsultationCard">
                        <h3 class="form-card-title">Request Service Setup</h3>
                        <p class="form-card-desc">Fill in details to get a dedicated deployment representative assigned to your project.</p>
                        <form id="quickConsultationForm" action="#" method="POST">
                            <input type="hidden" name="service" value="{service_name}">
                            <div class="form-group">
                                <label for="quickName" class="form-label">Full Name</label>
                                <input type="text" id="quickName" name="name" class="form-input" placeholder="e.g., Ramesh Kumar" required>
                            </div>
                            <div class="form-group">
                                <label for="quickPhone" class="form-label">Phone Number</label>
                                <input type="tel" id="quickPhone" name="phone" class="form-input" placeholder="e.g., +91 93692 88078" required>
                            </div>
                            <div class="form-group">
                                <label for="quickEmail" class="form-label">Email Address</label>
                                <input type="email" id="quickEmail" name="email" class="form-input" placeholder="e.g., name@company.com" required>
                            </div>
                            <div class="form-group">
                                <label for="quickComments" class="form-label">Specific Requirements (Optional)</label>
                                <textarea id="quickComments" name="comments" rows="4" class="form-textarea" placeholder="e.g., urgency timeline, locations..."></textarea>
                            </div>
                            <button type="submit" class="btn btn-gold btn-full-width">Submit Inquiry</button>
                        </form>
                        <div id="quickFormFeedback" class="form-feedback hide"></div>
                    </div>
                    
                    <a href="../services.html" class="back-to-hub-btn"><i class="fa-solid fa-arrow-left"></i> Back to Services Hub</a>
                </div>
            </aside>

        </div>
    </section>

    <!-- INTERACTIVE LEAD CAPTURE & FOOTER SECTION -->
    <section class="quote-section" id="quote-section">
        <div class="container">
            <div class="quote-container-grid">
                <!-- Form Box -->
                <div class="quote-form-wrapper scroll-fade">
                    <h2 class="quote-heading">Request Custom Quote</h2>
                    <p class="quote-subheading">Select services you need and we will prepare a specialized feasibility plan.</p>
                    
                    <!-- Multi-step form tracker -->
                    <div class="form-steps-indicator">
                        <div class="step-dot active" id="stepIndicator1"><span>1</span> Services</div>
                        <div class="step-line" id="stepLine1"></div>
                        <div class="step-dot" id="stepIndicator2"><span>2</span> Contact</div>
                        <div class="step-line" id="stepLine2"></div>
                        <div class="step-dot" id="stepIndicator3"><span>3</span> Submit</div>
                    </div>

                    <form id="multiStepQuoteForm" action="#" method="POST">
                        <!-- STEP 1: SERVICE CHECKBOXES -->
                        <div class="form-step-pane active" id="formStepPane1">
                            <h4 class="step-pane-title">Choose Services (Select all that apply)</h4>
                            <div class="checkbox-columns">
                                <div class="checkbox-group-block">
                                    <h5 class="checkbox-block-title">Legal Setup</h5>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="GST Registration" {checked_gst}>
                                        <span class="checkmark"></span> GST Registration
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="MSME/Udyam Registration" {checked_msme}>
                                        <span class="checkmark"></span> MSME / Udyam
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="FSSAI Registration" {checked_fssai}>
                                        <span class="checkmark"></span> FSSAI Food License
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="IEC Import Export Code" {checked_iec}>
                                        <span class="checkmark"></span> Import Export (IEC)
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Trademark Registration" {checked_trademark}>
                                        <span class="checkmark"></span> Trademark (TM/®)
                                    </label>
                                </div>
                                <div class="checkbox-group-block">
                                    <h5 class="checkbox-block-title">Quality & Licensing</h5>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="ISO Certification" {checked_iso}>
                                        <span class="checkmark"></span> ISO Certification
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="ZED Certification" {checked_zed}>
                                        <span class="checkmark"></span> ZED Green Cert
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="GeM Portal Registration" {checked_gem}>
                                        <span class="checkmark"></span> GeM Registration
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="BIS Certification" {checked_bis}>
                                        <span class="checkmark"></span> BIS Certification
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Trade License" {checked_trade}>
                                        <span class="checkmark"></span> Trade License
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Factory License" {checked_factory}>
                                        <span class="checkmark"></span> Factory License
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Solar Energy Service" {checked_solar}>
                                        <span class="checkmark"></span> Solar Energy Service
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="EPR Battery Registration" {checked_epr_battery}>
                                        <span class="checkmark"></span> Battery EPR Registration
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="EPR Tyre Registration" {checked_epr_tyre}>
                                        <span class="checkmark"></span> Tyre EPR Registration
                                    </label>
                                </div>
                                <div class="checkbox-group-block">
                                    <h5 class="checkbox-block-title">Other Verticals</h5>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Tender Bidding Advisory" {checked_tender}>
                                        <span class="checkmark"></span> Tender Consultancy
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Bank DPR Project Reports" {checked_dpr}>
                                        <span class="checkmark"></span> DPR Preparation
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Startup India Framework" {checked_startup}>
                                        <span class="checkmark"></span> Startup India
                                    </label>
                                    <label class="custom-checkbox">
                                         <input type="checkbox" name="services" value="Software App Development" {checked_software}>
                                         <span class="checkmark"></span> Software & App Dev
                                     </label>
                                     <label class="custom-checkbox">
                                         <input type="checkbox" name="services" value="ERP CRM Solutions" {checked_erp}>
                                         <span class="checkmark"></span> ERP & CRM Portals
                                     </label>
                                     <label class="custom-checkbox">
                                         <input type="checkbox" name="services" value="Cloud Cybersecurity" {checked_cloud}>
                                         <span class="checkmark"></span> Cloud & Cyber Security
                                     </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Website Engineering" {checked_web}>
                                        <span class="checkmark"></span> Web Engineering
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Digital Marketing Campaigns" {checked_marketing}>
                                        <span class="checkmark"></span> Digital Marketing
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Women Entrepreneur Advisory" {checked_women}>
                                        <span class="checkmark"></span> Women Mentorship
                                    </label>
                                    <label class="custom-checkbox">
                                        <input type="checkbox" name="services" value="Agriculture Business Services" {checked_agriculture}>
                                        <span class="checkmark"></span> Agriculture Services
                                    </label>
                                </div>
                            </div>
                            <div class="form-navigation">
                                <button type="button" class="btn btn-primary" id="btnNext1">Continue to Contact Info <i class="fa-solid fa-arrow-right"></i></button>
                            </div>
                        </div>

                        <!-- STEP 2: CONTACT INFO -->
                        <div class="form-step-pane" id="formStepPane2">
                            <h4 class="step-pane-title">Contact & Professional Details</h4>
                            <div class="form-row">
                                <div class="form-group flex-1">
                                    <label for="contactName" class="form-label">Full Name *</label>
                                    <input type="text" id="contactName" name="contactName" class="form-input" placeholder="e.g., Ramesh Kumar">
                                </div>
                                <div class="form-group flex-1">
                                    <label for="contactPhone" class="form-label">Phone Number *</label>
                                    <input type="tel" id="contactPhone" name="contactPhone" class="form-input" placeholder="e.g., +91 93692 88078">
                                </div>
                            </div>
                            <div class="form-row">
                                <div class="form-group flex-1">
                                    <label for="contactEmail" class="form-label">Email Address *</label>
                                    <input type="email" id="contactEmail" name="contactEmail" class="form-input" placeholder="e.g., ramesh@example.com">
                                </div>
                                <div class="form-group flex-1">
                                    <label for="contactLocation" class="form-label">Business City / Location *</label>
                                    <input type="text" id="contactLocation" name="contactLocation" class="form-input" placeholder="e.g., Kanpur, Uttar Pradesh">
                                </div>
                            </div>
                            <div class="form-navigation">
                                <button type="button" class="btn btn-secondary" id="btnPrev2"><i class="fa-solid fa-arrow-left"></i> Back</button>
                                <button type="button" class="btn btn-primary" id="btnNext2">Review & Write Message <i class="fa-solid fa-arrow-right"></i></button>
                            </div>
                        </div>

                        <!-- STEP 3: MESSAGE & SUBMIT -->
                        <div class="form-step-pane" id="formStepPane3">
                            <h4 class="step-pane-title">Brief Your Requirement</h4>
                            <div class="form-group">
                                <label for="contactMessage" class="form-label">Specific requirements or questions (Optional)</label>
                                <textarea id="contactMessage" name="contactMessage" rows="5" class="form-textarea" placeholder="Provide additional details regarding your setup, scale, or deadlines..."></textarea>
                            </div>
                            <div class="form-navigation">
                                <button type="button" class="btn btn-secondary" id="btnPrev3"><i class="fa-solid fa-arrow-left"></i> Back</button>
                                <button type="submit" class="btn btn-gold" id="btnSubmitQuote">Submit Final Request <i class="fa-solid fa-paper-plane"></i></button>
                            </div>
                        </div>
                    </form>
                    <div id="multiStepFormFeedback" class="form-feedback hide"></div>
                </div>

                <!-- Contact Info & Map Box -->
                <div class="quote-info-wrapper scroll-fade">
                    <div class="info-block">
                        <h3 class="info-block-title">Corporate Headquarters</h3>
                        <p class="info-block-detail"><i class="fa-solid fa-map-location-dot block-icon"></i> Kanpur, Uttar Pradesh, India</p>
                    </div>

                    <div class="info-block">
                        <h3 class="info-block-title">Call or Message Us</h3>
                        <p class="info-block-detail"><i class="fa-solid fa-phone block-icon"></i> <a href="tel:+919369288078">+91 9369288078</a></p>
                        <p class="info-block-detail"><i class="fa-solid fa-envelope block-icon"></i> <a href="mailto:jioliteproducts@gmail.com">jioliteproducts@gmail.com</a></p>
                    </div>

                    <div class="info-block">
                        <h3 class="info-block-title">Operational Working Hours</h3>
                        <p class="info-block-detail"><i class="fa-solid fa-clock block-icon"></i> Monday - Saturday: 10:00 AM - 07:00 PM</p>
                    </div>

                    <!-- Kanpur Map Embed -->
                    <div class="map-embed-wrapper">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d114312.44390610368!2d80.26421453303668!3d26.44741282276538!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399c4770b127c46f%3A0x1778302a9fbe7b41!2sKanpur%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1719112454652!5m2!1sen!2sin" width="100%" height="220" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER BRANDING -->
    <footer class="main-footer">
        <div class="container footer-container">
            <div class="footer-col-brand">
                <div class="footer-logo">
                    <img src="../assets/logo.png" alt="JPPL Logo" class="footer-logo-img">
                </div>
                <p class="footer-brand-tagline">JPPL Digital Services - Your Trusted Partner for End-to-End Business Solutions.</p>
                <p class="footer-brand-desc">Operating under Jio Lite Products Private Limited. We execute your legal registrations, secure industrial licensing, submit public bids, engineer web ecosystems, and coordinate healthcare logistics.</p>
                <div class="social-links">
                    <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
                    <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                    <a href="#" aria-label="Google"><i class="fa-brands fa-google"></i></a>
                </div>
            </div>

            <div class="footer-col-links">
                <h4 class="footer-title">Quick Links</h4>
                <ul class="footer-links-list">
                    <li><a href="../index.html"><i class="fa-solid fa-angle-right"></i> Home</a></li>
                    <li><a href="../about.html"><i class="fa-solid fa-angle-right"></i> About Us</a></li>
                    <li><a href="../services.html?cat=digital"><i class="fa-solid fa-angle-right"></i> IT Services</a></li>
                    <li><a href="#quote-section"><i class="fa-solid fa-angle-right"></i> Request Quote</a></li>
                </ul>
            </div>

            <div class="footer-col-links">
                <h4 class="footer-title">Our Verticals</h4>
                <ul class="footer-links-list">
                    <li><a href="../services.html?cat=legal"><i class="fa-solid fa-angle-right"></i> Business Setup</a></li>
                    <li><a href="../services.html?cat=quality"><i class="fa-solid fa-angle-right"></i> Quality Licensing</a></li>
                    <li><a href="../services.html?cat=capital"><i class="fa-solid fa-angle-right"></i> Capital Advisory</a></li>
                    <li><a href="../services.html?cat=digital"><i class="fa-solid fa-angle-right"></i> Digital Growth</a></li>
                    <li><a href="../services.html?cat=specialized"><i class="fa-solid fa-angle-right"></i> Specialized Advisory</a></li>
                </ul>
            </div>

            <div class="footer-col-contacts">
                <h4 class="footer-title">Direct Contacts</h4>
                <p class="footer-contact-item"><i class="fa-solid fa-phone"></i> +91 9369288078, +91 9336274060</p>
                <p class="footer-contact-item"><i class="fa-solid fa-envelope"></i> jioliteproducts@gmail.com</p>
                <p class="footer-contact-item"><i class="fa-solid fa-location-dot"></i> Kanpur, Uttar Pradesh, India</p>
            </div>
        </div>
        
        <div class="footer-copyright">
            <div class="container copyright-container">
                <p>&copy; 2026 JPPL Digital Services. All rights reserved. Operating under legal corporate frameworks.</p>
                <p>Designed and Engrained for Supreme Corporate Authority.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts (pointing up one folder level) -->
    <script src="../script.js"></script>
</body>
</html>
"""

# Create the services directory
os.makedirs('services', exist_ok=True)

# Helper function to generate related links content
def get_related_links_html(related_slugs):
    html = ""
    for r_slug in related_slugs:
        # Find related service name
        target = next((item for item in services_data if item["slug"] == r_slug), None)
        if target:
            html += f'''
            <a href="{target["slug"]}.html" class="related-card">
                <div class="related-card-icon"><i class="fa-solid {target["icon"]}"></i></div>
                <h4 class="related-card-title">{target["name"]}</h4>
                <span class="related-card-link">Learn More <i class="fa-solid fa-arrow-right"></i></span>
            </a>
            '''
    return html

# Helper function to get category-specific SEO keywords
def get_category_keywords(category):
    mapping = {
        "Business Setup & Registration Services": "GST registration, MSME Udyam registration, FSSAI food license, Import Export Code DGFT, Trademark registration, brand name filing",
        "Compliance & Industrial Licensing": "ISO certification standard, ZED green certification MSME, GeM portal registration, BIS certification India, municipal trade license, factory license registration",
        "Bidding & Capital Projects": "government tender bidding, e-tender submission service, bank project report DPR preparation, CMA data reports, Startup India recognition",
        "IT Services": "custom software development, mobile app development, iOS android apps, custom ERP system, CRM software portals, cloud computing, cybersecurity audit, website development Kanpur, corporate web design company, digital marketing agency, local SEO services",
        "Core Welfare & Healthcare Operations": "APEDA organic registration, organic farming certification, corporate wellness planner, NABL diagnostic report collections, women mentorship network"
    }
    return mapping.get(category, "corporate services, business registration, legal compliance")

# Main loop to write the 24 files
for svc in services_data:
    filename = f"services/{svc['slug']}.html"
    
    # Checkbox prep for bottom quote form (default check the current service page check)
    checked_vals = {
        "checked_gst": "checked" if svc["name"] == "GST Registration Service" else "",
        "checked_msme": "checked" if svc["name"] == "MSME / Udyam Registration Service" else "",
        "checked_fssai": "checked" if svc["name"] == "FSSAI Licensing Service" else "",
        "checked_iec": "checked" if svc["name"] == "IEC Import Export Service" else "",
        "checked_trademark": "checked" if svc["name"] == "Trademark Registration Service" else "",
        
        "checked_iso": "checked" if svc["name"] == "ISO Certification Service" else "",
        "checked_zed": "checked" if svc["name"] == "ZED Certification Service" else "",
        "checked_gem": "checked" if svc["name"] == "GeM Portal Registration Service" else "",
        "checked_bis": "checked" if svc["name"] == "BIS Certification Service" else "",
        "checked_trade": "checked" if svc["name"] == "Trade License Service" else "",
        "checked_factory": "checked" if svc["name"] == "Factory License Service" else "",
        "checked_solar": "checked" if svc["name"] == "Solar Energy Service" else "",
        "checked_epr_battery": "checked" if svc["name"] == "EPR Battery Waste Management Registration" else "",
        "checked_epr_tyre": "checked" if svc["name"] == "EPR Waste Tyre Management Registration" else "",
        
        "checked_tender": "checked" if svc["name"] == "Government Tender Submission Service" else "",
        "checked_dpr": "checked" if svc["name"] == "DPR / Project Report Preparation Service" else "",
        "checked_startup": "checked" if svc["name"] == "Startup India Recognition Service" else "",
        
        "checked_web": "checked" if svc["name"] == "Website Development Service" else "",
        "checked_marketing": "checked" if svc["name"] == "Performance Digital Marketing Service" else "",
        "checked_software": "checked" if svc["name"] == "Custom Software & App Development" else "",
        "checked_erp": "checked" if svc["name"] == "Custom ERP & CRM Solutions" else "",
        "checked_cloud": "checked" if svc["name"] == "Cloud Services & Cyber Security" else "",
        
        "checked_women": "checked" if svc["name"] == "Women Entrepreneur Framework Service" else "",
        "checked_financial": "checked" if svc["name"] == "Financial Planning Service" else "",
        "checked_healthcare": "checked" if svc["name"] == "Healthcare Operations Service" else "",
        "checked_lab": "checked" if svc["name"] == "Lab Diagnostics Service" else "",
        "checked_agriculture": "checked" if svc["name"] == "Agriculture Business Service" else "",
    }
    
    # Generate related HTML cards
    related_links_html = get_related_links_html(svc["related"])
    category_keywords = get_category_keywords(svc["category"])

    # Render template values
    page_html = PAGE_TEMPLATE.format(
        service_name=svc["name"],
        category=svc["category"],
        tagline=svc["tagline"],
        overview_brief=svc["overview"][:155] + "...",
        overview=svc["overview"],
        value=svc["value"],
        checklist_type=svc["checklist_type"],
        checklist_content=svc["checklist_content"],
        related_links=related_links_html,
        slug=svc["slug"],
        meta_keywords=category_keywords,
        image=svc["image"],
        **checked_vals
    )
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_html)

print(f"SUCCESS: {len(services_data)} individual HTML service files generated in 'services/' directory.")


