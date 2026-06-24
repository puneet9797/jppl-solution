import os

# Data structure containing information for all 20 services
services_data = [
    # Category A: Legal Setup & Registrations
    {
        "category": "Business Setup & Registration",
        "cat_slug": "legal",
        "name": "GST Registration",
        "slug": "gst-registration",
        "icon": "fa-scale-balanced",
        "tagline": "Simplify tax compliance for proprietorships, LLPs, and companies.",
        "overview": "Simplifying tax compliance is critical to commercial safety. We handle complete end-to-end registration for proprietorships, partnerships, LLPs, Private Limited companies, One Person Companies (OPC), and e-commerce sellers.",
        "value": "Grants your business a formal legal identity, unlocks Input Tax Credit (ITC), allows cross-border pan-India commerce, and qualifies your firm for prestigious Government Tenders and GeM registrations.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "PAN Card, Aadhaar Card, Business Address Proof (Rent Agreement or Utility Bill), Photo, and Bank Details.",
        "related": ["msme-udyam-registration", "fssai-food-license", "trademark-registration"]
    },
    {
        "category": "Business Setup & Registration",
        "cat_slug": "legal",
        "name": "MSME / Udyam Registration",
        "slug": "msme-udyam-registration",
        "icon": "fa-briefcase",
        "tagline": "Official government recognition for manufacturers and traders.",
        "overview": "Official government recognition for Micro, Small, and Medium Enterprises (Manufacturers, Service Providers, Traders, and Startups) under the Ministry of MSME.",
        "value": "Unlocks massive government subsidy benefits, lower interest rates on business bank loans, priority sector lending, collateral-free credit access, and faster processing of industrial approvals.",
        "checklist_type": "Processing Timeline",
        "checklist_content": "Guaranteed 1-Day processing and certificate delivery from final submission.",
        "related": ["gst-registration", "fssai-food-license", "startup-india-recognition"]
    },
    {
        "category": "Business Setup & Registration",
        "cat_slug": "legal",
        "name": "FSSAI Registration",
        "slug": "fssai-food-license",
        "icon": "fa-utensils",
        "tagline": "Mandatory food safety license for food business operators.",
        "overview": "Mandatory Food Safety License issued by the Food Safety and Standards Authority of India (FSSAI) for restaurants, hotels, cloud kitchens, grocery traders, and food processors.",
        "value": "Establishes complete legal compliance, builds consumer confidence in quality, avoids heavy municipal closures/penalties, and is strictly required to onboard onto online delivery platforms (Zomato/Swiggy).",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "Business address proof, identity proof, list of food categories, and layout map of the manufacturing site (for manufacturing licenses).",
        "related": ["gst-registration", "trade-licence", "factory-licence"]
    },
    {
        "category": "Business Setup & Registration",
        "cat_slug": "legal",
        "name": "IEC (Import Export Code)",
        "slug": "iec-import-export-code",
        "icon": "fa-plane-departure",
        "tagline": "Mandatory business identity code for cross-border trade.",
        "overview": "A mandatory 10-digit business identity code issued by the Directorate General of Foreign Trade (DGFT), Ministry of Commerce, for any entity engaging in cross-border import and export.",
        "value": "Grants your business global marketplace access, enables seamless import/export shipments, and allows your firm to claim attractive government export incentive schemes.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "PAN Card of the entity, bank certificate or canceled check, address proof of business.",
        "related": ["gst-registration", "trademark-registration", "iso-certification"]
    },
    {
        "category": "Business Setup & Registration",
        "cat_slug": "legal",
        "name": "Trademark Registration (TM / ®)",
        "slug": "trademark-registration",
        "icon": "fa-registered",
        "tagline": "Long-term brand protection legally safeguarding taglines and logos.",
        "overview": "Long-term brand protection that legally safeguards your unique brand name, logo, design symbols, or corporate tagline under the Trademarks Act.",
        "value": "Delivers exclusive legal ownership, prevents copycats from diluting your market reputation, and builds valuable intangible business equity over its 10-year renewable validity.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "Logo/brand name copy, identity proof of applicant, Power of Attorney authorization document.",
        "related": ["gst-registration", "iec-import-export-code", "startup-india-recognition"]
    },
    
    # Category B: Quality Assurance & Corporate Licensing
    {
        "category": "Quality Assurance & Corporate Licensing",
        "cat_slug": "quality",
        "name": "ISO Certification",
        "slug": "iso-certification",
        "icon": "fa-certificate",
        "tagline": "Globally recognized quality management standards.",
        "overview": "Internationally recognized quality standard certifications (such as ISO 9001 for quality, ISO 14001 for environment, and ISO 27001 for security) confirming your firm's compliance.",
        "value": "Maximizes your business reputation, validates operational efficiency and safety to global consumers, and satisfies core eligibility criteria for large-scale corporate and government bids.",
        "checklist_type": "Required Audit Documents",
        "checklist_content": "Business registration copy, scope of work description, standard operating procedures checklist, and brief organizational chart.",
        "related": ["zed-green-certification", "bis-standards-certification", "gem-portal-registration"]
    },
    {
        "category": "Quality Assurance & Corporate Licensing",
        "cat_slug": "quality",
        "name": "ZED Certification (Zero Defect Zero Effect)",
        "slug": "zed-green-certification",
        "icon": "fa-leaf",
        "tagline": "Specialized green manufacturing certification framework.",
        "overview": "A specialized green manufacturing certification framework curated by the Ministry of MSME, Government of India, exclusively for manufacturing MSMEs to reduce waste.",
        "value": "Dramatically improves factory productivity, minimizes manufacturing defects, and provides priority access to specific government credit incentives, clean energy grants, and concession rates.",
        "checklist_type": "Statutory Eligibility",
        "checklist_content": "Available only to MSMEs with a valid Udyam Registration engaged in active manufacturing operations.",
        "related": ["msme-udyam-registration", "iso-certification", "factory-licence"]
    },
    {
        "category": "Quality Assurance & Corporate Licensing",
        "cat_slug": "quality",
        "name": "GeM (Government e-Marketplace) Registration",
        "slug": "gem-portal-registration",
        "icon": "fa-cart-shopping",
        "tagline": "Centralized procurement portal for public ministries and departments.",
        "overview": "Direct registration and product mapping to list your company's products and services on India's centralized public procurement portal for ministries and government departments.",
        "value": "Opens the door to secure direct, paperless government purchase orders, participate in transparent public bidding, and access highly predictable government payment cycles.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "PAN, Aadhaar, GST Certificate, Bank Account Details, and active Udyam Certificate (if applicable).",
        "related": ["gst-registration", "msme-udyam-registration", "government-tender-consultancy"]
    },
    {
        "category": "Quality Assurance & Corporate Licensing",
        "cat_slug": "quality",
        "name": "BIS Certification",
        "slug": "bis-standards-certification",
        "icon": "fa-award",
        "tagline": "Product conformity and safety standards by Bureau of Indian Standards.",
        "overview": "Product conformity and standard safety certification issued by the Bureau of Indian Standards (BIS) confirming manufacturing benchmarks and reliability.",
        "value": "Guarantees raw material and product safety, mandates regulatory compliance for manufacturing market entry in India, and builds concrete consumer confidence.",
        "checklist_type": "Audit & Lab Testing",
        "checklist_content": "Requires factory raw-material inspection, sample collections, and laboratory testing at BIS recognized labs.",
        "related": ["iso-certification", "zed-green-certification", "factory-licence"]
    },
    {
        "category": "Quality Assurance & Corporate Licensing",
        "cat_slug": "quality",
        "name": "Trade Licence",
        "slug": "trade-licence",
        "icon": "fa-house-medical",
        "tagline": "Municipal operating permission for commercial establishments.",
        "overview": "Official operating permission obtained from local municipal corporations or urban authorities to establish regular commercial activities in a specific area.",
        "value": "Ensures your day-to-day operations align with local municipal bylaws, helping your business avoid unexpected administrative closures, closures due to zoning, or legal penalties.",
        "checklist_type": "Required Checklist / Documents",
        "checklist_content": "Sanction layout plan, property tax receipt, municipal occupancy certificate, lease agreement, and NOC from immediate neighbors.",
        "related": ["factory-licence", "gst-registration", "fssai-food-license"]
    },
    {
        "category": "Quality Assurance & Corporate Licensing",
        "cat_slug": "quality",
        "name": "Factory Licence",
        "slug": "factory-licence",
        "icon": "fa-industry",
        "tagline": "Statutory safety registration for manufacturing plants.",
        "overview": "Statutory compliance registration required for industrial manufacturing units, engineering outfits, and chemical plants operating under the Factories Act.",
        "value": "Protects worker safety, satisfies labor law compliance parameters, and secures clean governmental approval to operate machinery and layout plans.",
        "checklist_type": "Required Approvals",
        "checklist_content": "Requires prior Factory Plan approval, NOC from Pollution Control Board, Fire Safety NOC, and stability certificate of the building structure.",
        "related": ["trade-licence", "bis-standards-certification", "zed-green-certification"]
    },
    
    # Category C: Strategic Capital & Government Bids
    {
        "category": "Government & Capital Advisory",
        "cat_slug": "capital",
        "name": "Government Tender Consultancy",
        "slug": "government-tender-consultancy",
        "icon": "fa-file-invoice-dollar",
        "tagline": "End-to-end guidance through public bidding frameworks.",
        "overview": "End-to-end guidance through the bureaucratic landscape of public bidding, government auctions, and requests for proposals (RFPs) on state and national portals.",
        "value": "Includes exhaustive tender searching, precision documentation compilation, technical bid optimization, and financial bid submission strategies to dramatically scale your bid success rate.",
        "checklist_type": "Consultancy Phase Layout",
        "checklist_content": "Includes Tender Search, Bid Preparation, Class 3 Digital Signature Setup, Technical Query Submissions, and Financial Bidding Strategy.",
        "related": ["gem-portal-registration", "dpr-project-report-preparation", "iso-certification"]
    },
    {
        "category": "Government & Capital Advisory",
        "cat_slug": "capital",
        "name": "DPR / Project Report Preparation",
        "slug": "dpr-project-report-preparation",
        "icon": "fa-file-circle-check",
        "tagline": "Bank-grade Detailed Project Reports and CMA calculations.",
        "overview": "Engineering detailed, accurate bank-grade Detailed Project Reports (DPR), MSME industrial project profiles, and comprehensive CMA data sheets.",
        "value": "Perfect for optimizing commercial bank loan approvals, creating bulletproof investor presentations, and securing capital under government credit-linked subsidy schemes.",
        "checklist_type": "Report Deliverables",
        "checklist_content": "Includes Market Feasibility analysis, Financial Model forecasts (5-10 years), Balance Sheet projection sheets, CMA Data files, and Cash Flow calculations.",
        "related": ["financial-advisory-services", "government-tender-consultancy", "startup-india-recognition"]
    },
    {
        "category": "Government & Capital Advisory",
        "cat_slug": "capital",
        "name": "Startup India Recognition",
        "slug": "startup-india-recognition",
        "icon": "fa-rocket",
        "tagline": "Premium government accreditation for innovative business models.",
        "overview": "A premium government-issued accreditation certifying your innovative business model under the national Startup India initiative by DPIIT.",
        "value": "Open to innovative business models (under 10 years old with turnover under 100 Crore), offering multi-year tax exemptions, fast-tracked patent filings, self-compliance benefits, and access to government venture funds.",
        "checklist_type": "Eligibility Criteria",
        "checklist_content": "Must be incorporated as a Private Limited, LLP, or registered Partnership. Must show innovation, scalability, and product development potential.",
        "related": ["msme-udyam-registration", "trademark-registration", "dpr-project-report-preparation"]
    },
    
    # Category D: Digital Engineering & Marketing Ecosystem
    {
        "category": "Digital Growth Solutions",
        "cat_slug": "digital",
        "name": "Website Development Services",
        "slug": "website-development-services",
        "icon": "fa-laptop-code",
        "tagline": "High-conversion responsive corporate web development.",
        "overview": "Building high-conversion corporate digital real estate. Includes custom responsive layouts, e-commerce storefronts, highly optimized landing pages, and ongoing code maintenance.",
        "value": "Optimizes your business visibility with fast-loading, SEO-friendly architectures, professional business email setups, and verified Google My Business (GMB) map configurations.",
        "checklist_type": "Engineering Deliverables",
        "checklist_content": "Custom UI design mockup, clean HTML5/CSS/JS development, Domain & hosting setup, SSL security integration, and search engine registrations.",
        "related": ["digital-marketing-services", "trademark-registration", "startup-india-recognition"]
    },
    {
        "category": "Digital Growth Solutions",
        "cat_slug": "digital",
        "name": "Digital Marketing Services",
        "slug": "digital-marketing-services",
        "icon": "fa-share-nodes",
        "tagline": "Data-driven social media and search ads lead pipelines.",
        "overview": "Data-driven digital marketing campaigns across major search engines and social platforms (Facebook, Instagram, LinkedIn, Google Ads, YouTube).",
        "value": "Builds massive brand awareness, drives consistent lead-generation pipelines, and maximizes client retention through transparent measurable analytics.",
        "checklist_type": "Services Scope",
        "checklist_content": "Includes Social Media Management (SMM), Search Engine Optimization (SEO), PPC Ad Campaign runs, Content design, and analytics mapping.",
        "related": ["website-development-services", "financial-advisory-services", "trademark-registration"]
    },
    
    # Category E: Specialized Consulting & Welfare Solutions
    {
        "category": "Individual & Specialized Advisory",
        "cat_slug": "specialized",
        "name": "Women Entrepreneur Consultant (WEC)",
        "slug": "women-entrepreneur-consultant",
        "icon": "fa-female",
        "tagline": "Mentorship and government grant alignment for female business leaders.",
        "overview": "A dedicated framework offering specialized corporate mentorship, dedicated funding alignment, and grant access specifically curated for women-led enterprises.",
        "value": "Empowers female leaders with industry networking circles, government grant support schemes (e.g., Mudra, Mahila Co-op), and customized industrial business training modules.",
        "checklist_type": "Specialized Support",
        "checklist_content": "Access to Mahila-centric bank schemes, specific interest subsidy lists, and direct startup advisory panels.",
        "related": ["msme-udyam-registration", "financial-advisory-services", "startup-india-recognition"]
    },
    {
        "category": "Individual & Specialized Advisory",
        "cat_slug": "specialized",
        "name": "Financial Advisory Services (FAS)",
        "slug": "financial-advisory-services",
        "icon": "fa-chart-line",
        "tagline": "Asset optimization, tax planning, and cash flow structures.",
        "overview": "Tailored asset management, operational liquidity advisory, and legal tax compliance consulting for individuals and corporate entities.",
        "value": "Specializes in systematic wealth growth, legal tax optimization strategies, meticulous cash flow forecasting, and structured capital advisory for corporate expansions.",
        "checklist_type": "Core Solutions",
        "checklist_content": "Asset Allocation models, Corporate Tax advisory, Working Capital optimization, and Debt structure advisory.",
        "related": ["dpr-project-report-preparation", "women-entrepreneur-consultant", "healthcare-services"]
    },
    {
        "category": "Individual & Specialized Advisory",
        "cat_slug": "specialized",
        "name": "Healthcare Services (HS)",
        "slug": "healthcare-services",
        "icon": "fa-heartpulse",
        "tagline": "Corporate wellness planning and medical safety blueprints.",
        "overview": "Comprehensive medical checkup design, preventive immunization planning, and targeted physical wellness coordination for families and corporate teams.",
        "value": "Delivers complete medical safety blueprints, emergency planning protocols, and sustainable, long-term health programs for employee retention.",
        "checklist_type": "Advisory Scope",
        "checklist_content": "Corporate wellness packages, statutory compliance checklist for work safety, and emergency response training setups.",
        "related": ["lab-corp-services", "financial-advisory-services", "women-entrepreneur-consultant"]
    },
    {
        "category": "Individual & Specialized Advisory",
        "cat_slug": "specialized",
        "name": "Lab Corp Services (LCS)",
        "slug": "lab-corp-services",
        "icon": "fa-flask-vial",
        "tagline": "NABL Niche diagnostic test collections and corporate health reporting.",
        "overview": "Ultra-fast, highly precise diagnostic testing networks operating under stringent NABL and CAP quality control standards.",
        "value": "Offers frictionless sample home collection options, state-of-the-art technological precision, fast digital report turnarounds, and tailored wellness tracking databases.",
        "checklist_type": "Quality Specifications",
        "checklist_content": "Certified under NABL (National Accreditation Board for Testing and Calibration Laboratories) guidelines to assure report precision.",
        "related": ["healthcare-services", "financial-advisory-services", "women-entrepreneur-consultant"]
    }
]

# Base template HTML code for services
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{overview_brief}">
    <title>{service_name} | JPPL Solutions</title>
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
                <div class="logo-text">
                    <span class="logo-title">JPPL</span>
                    <span class="logo-subtitle">Solutions</span>
                </div>
            </a>

            <!-- Mobile Navigation Menu Toggle -->
            <button class="mobile-nav-toggle" id="mobileNavToggle" aria-label="Toggle navigation">
                <span class="hamburger"></span>
            </button>

            <!-- Navigation Links -->
            <nav class="nav-menu" id="navMenu">
                <ul class="nav-list">
                    <li class="nav-item"><a href="../index.html" class="nav-link">Home</a></li>
                    <li class="nav-item"><a href="../index.html#about-section" class="nav-link">About Us</a></li>
                    
                    <!-- Mega Menu Dropdown -->
                    <li class="nav-item has-mega-menu">
                        <a href="../services.html" class="nav-link dropdown-trigger active">Services <i class="fa-solid fa-chevron-down nav-chevron"></i></a>
                        <div class="mega-menu" id="megaMenu">
                            <div class="container mega-menu-grid">
                                <!-- Col 1: Business Setup -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-briefcase col-icon"></i> Legal Setup</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="gst-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> GST Registration</a></li>
                                        <li><a href="msme-udyam-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> MSME / Udyam</a></li>
                                        <li><a href="fssai-food-license.html"><i class="fa-solid fa-chevron-right link-bullet"></i> FSSAI Food License</a></li>
                                        <li><a href="iec-import-export-code.html"><i class="fa-solid fa-chevron-right link-bullet"></i> IEC Import Export</a></li>
                                        <li><a href="trademark-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Trademark Protection</a></li>
                                    </ul>
                                </div>
                                <!-- Col 2: Licensing -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-certificate col-icon"></i> Quality & Licensing</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="iso-certification.html"><i class="fa-solid fa-chevron-right link-bullet"></i> ISO Certification</a></li>
                                        <li><a href="zed-green-certification.html"><i class="fa-solid fa-chevron-right link-bullet"></i> ZED Green Certification</a></li>
                                        <li><a href="gem-portal-registration.html"><i class="fa-solid fa-chevron-right link-bullet"></i> GeM Registration</a></li>
                                        <li><a href="bis-standards-certification.html"><i class="fa-solid fa-chevron-right link-bullet"></i> BIS Standards</a></li>
                                        <li><a href="trade-licence.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Trade License</a></li>
                                        <li><a href="factory-licence.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Factory License</a></li>
                                    </ul>
                                </div>
                                <!-- Col 3: Capital Advisory -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-landmark col-icon"></i> Capital Advisory</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="government-tender-consultancy.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Government Tenders</a></li>
                                        <li><a href="dpr-project-report-preparation.html"><i class="fa-solid fa-chevron-right link-bullet"></i> DPR & Bank Projects</a></li>
                                        <li><a href="startup-india-recognition.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Startup India Recognition</a></li>
                                    </ul>
                                </div>
                                <!-- Col 4: Digital Growth -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-laptop-code col-icon"></i> Digital Growth</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="website-development-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Website Engineering</a></li>
                                        <li><a href="digital-marketing-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Digital Marketing</a></li>
                                    </ul>
                                </div>
                                <!-- Col 5: Specialized -->
                                <div class="mega-menu-col">
                                    <h4 class="mega-menu-title"><i class="fa-solid fa-handshake col-icon"></i> Specialized Services</h4>
                                    <ul class="mega-menu-links">
                                        <li><a href="women-entrepreneur-consultant.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Women Mentorship</a></li>
                                        <li><a href="financial-advisory-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Financial Advisory</a></li>
                                        <li><a href="healthcare-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Corporate Health</a></li>
                                        <li><a href="lab-corp-services.html"><i class="fa-solid fa-chevron-right link-bullet"></i> Lab Diagnostics (NABL)</a></li>
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
                        <h3 class="form-card-title">Enquire For This Service</h3>
                        <p class="form-card-desc">Fill details to get a dedicated compliance representative assigned to your project.</p>
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
                    <div class="footer-logo-text">
                        <span class="footer-logo-title">JPPL</span>
                        <span class="footer-logo-subtitle">Solutions</span>
                    </div>
                </div>
                <p class="footer-brand-tagline">JPPL SOLUTIONS - Your Trusted Partner for End-to-End Business Solutions.</p>
                <p class="footer-brand-desc">Also operating as JPPL Consultancy Services. We deliver authoritative corporate setup, industrial quality licensing, tender consulting, website engineering, and consumer-centric health tracking systems.</p>
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
                    <li><a href="../index.html#about-section"><i class="fa-solid fa-angle-right"></i> About Us</a></li>
                    <li><a href="../services.html"><i class="fa-solid fa-angle-right"></i> Services Hub</a></li>
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
                <p>&copy; 2026 JPPL Solutions. All rights reserved. Operating under legal corporate frameworks.</p>
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

# Main loop to write the 20 files
for svc in services_data:
    filename = f"services/{svc['slug']}.html"
    
    # Checkbox prep for bottom quote form (default check the current service page check)
    checked_vals = {
        "checked_gst": "checked" if svc["name"] == "GST Registration" else "",
        "checked_msme": "checked" if svc["name"] == "MSME / Udyam Registration" else "",
        "checked_fssai": "checked" if svc["name"] == "FSSAI Registration" else "",
        "checked_iec": "checked" if svc["name"] == "IEC (Import Export Code)" else "",
        "checked_trademark": "checked" if svc["name"] == "Trademark Registration (TM / ®)" else "",
        
        "checked_iso": "checked" if svc["name"] == "ISO Certification" else "",
        "checked_zed": "checked" if svc["name"] == "ZED Certification (Zero Defect Zero Effect)" else "",
        "checked_gem": "checked" if svc["name"] == "GeM (Government e-Marketplace) Registration" else "",
        "checked_bis": "checked" if svc["name"] == "BIS Certification" else "",
        "checked_trade": "checked" if svc["name"] == "Trade Licence" else "",
        "checked_factory": "checked" if svc["name"] == "Factory Licence" else "",
        
        "checked_tender": "checked" if svc["name"] == "Government Tender Consultancy" else "",
        "checked_dpr": "checked" if svc["name"] == "DPR / Project Report Preparation" else "",
        "checked_startup": "checked" if svc["name"] == "Startup India Recognition" else "",
        
        "checked_web": "checked" if svc["name"] == "Website Development Services" else "",
        "checked_marketing": "checked" if svc["name"] == "Digital Marketing Services" else "",
        
        "checked_women": "checked" if svc["name"] == "Women Entrepreneur Consultant (WEC)" else "",
        "checked_financial": "checked" if svc["name"] == "Financial Advisory Services (FAS)" else "",
        "checked_healthcare": "checked" if svc["name"] == "Healthcare Services (HS)" else "",
        "checked_lab": "checked" if svc["name"] == "Lab Corp Services (LCS)" else "",
    }
    
    # Generate related HTML cards
    related_links_html = get_related_links_html(svc["related"])

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
        **checked_vals
    )
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_html)

print("SUCCESS: 20 individual HTML service files generated in 'services/' directory.")
