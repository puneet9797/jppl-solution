/* ==========================================
   JPPL SOLUTIONS - INTERACTIVE LOGIC
   Vanilla Javascript for Client-Side Operations
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {

    // 1. STICKY NAVBAR SCROLL ACTION
    const mainHeader = document.getElementById('mainHeader');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            mainHeader.classList.add('scrolled');
        } else {
            mainHeader.classList.remove('scrolled');
        }
    });

    // 2. MOBILE NAVIGATION HAMBURGER TOGGLE
    const mobileNavToggle = document.getElementById('mobileNavToggle');
    const navMenu = document.getElementById('navMenu');

    if (mobileNavToggle && navMenu) {
        mobileNavToggle.addEventListener('click', () => {
            mobileNavToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close mobile nav when link is clicked
        const navLinks = document.querySelectorAll('.nav-link:not(.dropdown-trigger)');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileNavToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // Mobile Mega-Menu Toggle (click to open on mobile screens)
    const dropdownTrigger = document.querySelector('.dropdown-trigger');
    if (dropdownTrigger) {
        dropdownTrigger.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                const parent = dropdownTrigger.parentElement;
                parent.classList.toggle('open-mobile');
            }
        });
    }


    // 3. QUICK CONSULTATION FORM (HERO PAGE)
    const quickForm = document.getElementById('quickConsultationForm');
    const quickFeedback = document.getElementById('quickFormFeedback');

    if (quickForm) {
        quickForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const name = document.getElementById('quickName').value.trim();
            const phone = document.getElementById('quickPhone').value.trim();
            const serviceEl = document.getElementById('quickService');
            const service = serviceEl ? serviceEl.value : document.querySelector('input[name="service"]').value;

            if (!name || !phone || !service) {
                showFeedback(quickFeedback, 'Please fill in all details.', 'error');
                return;
            }

            // Simulate form submission
            showFeedback(quickFeedback, 'Sending request...', 'success');
            
            setTimeout(() => {
                showFeedback(quickFeedback, `Thank you, ${name}! Our team will call you back on ${phone} regarding ${service}.`, 'success');
                quickForm.reset();
            }, 1200);
        });
    }

    function showFeedback(element, message, type) {
        element.textContent = message;
        element.className = `form-feedback ${type}`;
        element.classList.remove('hide');
    }


    // 4. ACCORDION PANELS ON SERVICES PAGE
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    
    accordionHeaders.forEach(header => {
        header.addEventListener('click', () => {
            const card = header.parentElement;
            
            // Toggle open class on current clicked card
            card.classList.toggle('open');
        });
    });


    // 5. DOUBLE-SIDED CHECKBOX SYNCHRONIZATION (SERVICES & FOOTER FORM)
    const syncCheckboxes = document.querySelectorAll('.quote-sync-check');
    const formCheckboxes = document.querySelectorAll('#multiStepQuoteForm input[type="checkbox"][name="services"]');
    const selectionCountText = document.getElementById('selectionCountText');

    // Function to calculate and update selection count badge
    function updateSelectionState() {
        const checkedFormBoxes = document.querySelectorAll('#multiStepQuoteForm input[type="checkbox"][name="services"]:checked');
        const count = checkedFormBoxes.length;

        if (selectionCountText) {
            if (count === 0) {
                selectionCountText.textContent = "No services selected yet.";
            } else if (count === 1) {
                selectionCountText.textContent = "1 service selected.";
            } else {
                selectionCountText.textContent = `${count} services selected.`;
            }
        }
    }

    // Sync from Card Checkbox to Footer Form Checkbox
    syncCheckboxes.forEach(cardCheck => {
        cardCheck.addEventListener('change', () => {
            const serviceName = cardCheck.getAttribute('data-service-name');
            const bottomCheck = document.querySelector(`#multiStepQuoteForm input[type="checkbox"][value="${serviceName}"]`);
            
            if (bottomCheck) {
                bottomCheck.checked = cardCheck.checked;
            }
            
            // Highlight parent label
            const label = cardCheck.closest('.quote-check-label');
            if (label) {
                if (cardCheck.checked) {
                    label.classList.add('selected');
                } else {
                    label.classList.remove('selected');
                }
            }

            updateSelectionState();
        });
    });

    // Sync from Footer Form Checkbox back to Card Checkbox
    formCheckboxes.forEach(formCheck => {
        formCheck.addEventListener('change', () => {
            const serviceName = formCheck.value;
            const cardCheck = document.querySelector(`.quote-sync-check[data-service-name="${serviceName}"]`);
            
            if (cardCheck) {
                cardCheck.checked = formCheck.checked;
                
                // Highlight label on card
                const label = cardCheck.closest('.quote-check-label');
                if (label) {
                    if (formCheck.checked) {
                        label.classList.add('selected');
                    } else {
                        label.classList.remove('selected');
                    }
                }
            }

            updateSelectionState();
        });
    });


    // 6. MULTI-STEP LEAD CAPTURE FORM LOGIC
    const btnNext1 = document.getElementById('btnNext1');
    const btnNext2 = document.getElementById('btnNext2');
    const btnPrev2 = document.getElementById('btnPrev2');
    const btnPrev3 = document.getElementById('btnPrev3');
    const formStepPane1 = document.getElementById('formStepPane1');
    const formStepPane2 = document.getElementById('formStepPane2');
    const formStepPane3 = document.getElementById('formStepPane3');

    const stepIndicator1 = document.getElementById('stepIndicator1');
    const stepIndicator2 = document.getElementById('stepIndicator2');
    const stepIndicator3 = document.getElementById('stepIndicator3');
    const stepLine1 = document.getElementById('stepLine1');
    const stepLine2 = document.getElementById('stepLine2');

    // Transition helper between form steps
    function navigateToStep(hidePane, showPane, currentIndicator, nextIndicator, lineToComplete) {
        hidePane.classList.remove('active');
        showPane.classList.add('active');

        if (lineToComplete) {
            lineToComplete.classList.add('completed');
        } else if (currentIndicator && currentIndicator.id === 'stepIndicator2') {
            // we are moving back from step 2 to 1
            if (stepLine1) stepLine1.classList.remove('completed');
        } else if (currentIndicator && currentIndicator.id === 'stepIndicator3') {
            // we are moving back from step 3 to 2
            if (stepLine2) stepLine2.classList.remove('completed');
        }

        if (currentIndicator) currentIndicator.classList.remove('active');
        if (currentIndicator && lineToComplete) currentIndicator.classList.add('completed');
        if (nextIndicator) {
            nextIndicator.classList.remove('completed');
            nextIndicator.classList.add('active');
        }
    }

    if (btnNext1) {
        btnNext1.addEventListener('click', () => {
            // Step 1 check: user can continue even without selections, but warning alert or confirmation is nice.
            const selectedServices = document.querySelectorAll('#multiStepQuoteForm input[type="checkbox"][name="services"]:checked');
            navigateToStep(formStepPane1, formStepPane2, stepIndicator1, stepIndicator2, stepLine1);
        });
    }

    if (btnPrev2) {
        btnPrev2.addEventListener('click', () => {
            navigateToStep(formStepPane2, formStepPane1, stepIndicator2, stepIndicator1, null);
        });
    }

    if (btnNext2) {
        btnNext2.addEventListener('click', () => {
            // Validate inputs in step 2
            const name = document.getElementById('contactName').value.trim();
            const phone = document.getElementById('contactPhone').value.trim();
            const email = document.getElementById('contactEmail').value.trim();
            const location = document.getElementById('contactLocation').value.trim();

            if (!name || !phone || !email || !location) {
                alert('Please fill in all required contact details before moving forward.');
                return;
            }

            // Basic email validation regex
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                alert('Please enter a valid email address.');
                return;
            }

            navigateToStep(formStepPane2, formStepPane3, stepIndicator2, stepIndicator3, stepLine2);
        });
    }

    if (btnPrev3) {
        btnPrev3.addEventListener('click', () => {
            navigateToStep(formStepPane3, formStepPane2, stepIndicator3, stepIndicator2, null);
        });
    }

    // Form Submission
    const quoteForm = document.getElementById('multiStepQuoteForm');
    const formFeedback = document.getElementById('multiStepFormFeedback');

    if (quoteForm) {
        quoteForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('contactName').value.trim();
            const phone = document.getElementById('contactPhone').value.trim();
            const email = document.getElementById('contactEmail').value.trim();
            const location = document.getElementById('contactLocation').value.trim();
            const message = document.getElementById('contactMessage').value.trim();

            const selectedServices = [];
            document.querySelectorAll('#multiStepQuoteForm input[type="checkbox"][name="services"]:checked').forEach(cb => {
                selectedServices.push(cb.value);
            });

            // Submission Feedback
            showFeedback(formFeedback, 'Submitting quote request...', 'success');
            
            setTimeout(() => {
                showFeedback(formFeedback, `Thank you, ${name}! Your detailed request regarding ${selectedServices.length > 0 ? selectedServices.length : 'general'} services has been logged. We will reach out at ${email} shortly.`, 'success');
                
                // Complete the final step indicator state
                if (stepIndicator3) stepIndicator3.classList.add('completed');
                
                quoteForm.reset();
                // Reset sync checks labels
                document.querySelectorAll('.quote-check-label').forEach(label => label.classList.remove('selected'));
                updateSelectionState();

                // Go back to step 1 panel after reset
                setTimeout(() => {
                    navigateToStep(formStepPane3, formStepPane1, stepIndicator3, stepIndicator1, null);
                    if (stepIndicator1) stepIndicator1.className = "step-dot active";
                    if (stepIndicator2) stepIndicator2.className = "step-dot";
                    if (stepIndicator3) stepIndicator3.className = "step-dot";
                    if (stepLine1) stepLine1.classList.remove('completed');
                    if (stepLine2) stepLine2.classList.remove('completed');
                    formFeedback.classList.add('hide');
                }, 4000);

            }, 1500);
        });
    }


    // 7. SERVICES PAGE SIDEBAR TAB CLICKS & SCROLL SPY
    const tabLinks = document.querySelectorAll('.sidebar-tab-link');
    const categoryBlocks = document.querySelectorAll('.category-block');

    if (tabLinks.length > 0 && categoryBlocks.length > 0) {
        
        // Click action to scroll to sections smoothly
        tabLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetSec = document.querySelector(targetId);
                
                if (targetSec) {
                    targetSec.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // ScrollSpy mechanism: Highlight sidebar category tabs based on active scroll viewport
        window.addEventListener('scroll', () => {
            let activeId = '';
            const scrollPos = window.scrollY + 180; // offset spacing for header + navbar

            categoryBlocks.forEach(sec => {
                const secTop = sec.offsetTop;
                const secHeight = sec.offsetHeight;
                
                if (scrollPos >= secTop && scrollPos < secTop + secHeight) {
                    activeId = sec.getAttribute('id');
                }
            });

            tabLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${activeId}`) {
                    link.classList.add('active');
                }
            });
        });
    }


    // 8. INTERSECTION OBSERVER FOR SCROLL ANIMATIONS (FADE IN UP)
    const fadeElements = document.querySelectorAll('.scroll-fade');
    
    if ('IntersectionObserver' in window && fadeElements.length > 0) {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target); // trigger animation only once
                }
            });
        }, observerOptions);

        fadeElements.forEach(el => observer.observe(el));
    } else {
        // Fallback for older browsers
        fadeElements.forEach(el => el.classList.add('visible'));
    }


    // 9. AUTOMATIC LINK PARAMETER ROUTING (FROM MEGA MENU TO SPECIFIC ACCORDION / CATEGORY)
    const urlParams = new URLSearchParams(window.location.search);
    const categoryParam = urlParams.get('cat');
    
    if (categoryParam) {
        // Find section mapping
        let targetId = '';
        if (categoryParam === 'legal') targetId = '#category-legal';
        else if (categoryParam === 'quality') targetId = '#category-quality';
        else if (categoryParam === 'capital') targetId = '#category-capital';
        else if (categoryParam === 'digital') targetId = '#category-digital';
        else if (categoryParam === 'specialized') targetId = '#category-specialized';

        if (targetId) {
            setTimeout(() => {
                const targetSec = document.querySelector(targetId);
                if (targetSec) {
                    targetSec.scrollIntoView({ behavior: 'smooth' });
                }
            }, 300);
        }
    }

    // Auto expand accordion if anchor exists in URL hash (e.g. services.html#gst)
    if (window.location.hash) {
        const hashId = window.location.hash;
        setTimeout(() => {
            const card = document.querySelector(hashId);
            if (card && card.classList.contains('service-accordion-card')) {
                card.classList.add('open');
                card.scrollIntoView({ behavior: 'smooth' });
            }
        }, 500);
    }
});
