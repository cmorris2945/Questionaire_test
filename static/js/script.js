//const selections = {};
const totalQuestions = 19;
document.addEventListener('DOMContentLoaded', function() {
    const consentForm = document.getElementById('consentForm');
    const patientForm = document.getElementById('patientForm');
    const agreeConsentBtn = document.getElementById('agreeConsent');
    const consentName = document.getElementById('consentName');
    const consentDate = document.getElementById('consentDate');
    const patientName = document.getElementById('consentName'); // Assuming this is the ID of the name field in the main form
    const firstQuestion = document.getElementById('question0');
    const chatBotHeader = document.getElementById('chatbot-header');
    const consentHeader = document.getElementById('consentHeader');
    const chatContainer = document.getElementById('chat-container');
    const topNavBar = document.getElementById('topNavBar');
    const body = document.getElementsByTagName("body")[0];
    // Set current date automatically
    const currentDate = new Date().toISOString().split('T')[0];
    consentDate.value = currentDate;

    // Consent form handling
    agreeConsentBtn.addEventListener('click', function(event) {
        event.preventDefault();
        if (consentName.value.trim() === '') {
            alert('Please fill in your name to give consent.');
            return;
        }
        consentForm.style.display = 'none';
        //patientForm.style.display = 'block';
        firstQuestion.style.display = 'block';
        chatBotHeader.style.display = 'block';
        consentHeader.style.display = 'none';
        chatContainer.style.display = 'block';
        topNavBar.style.display = 'none';
        body.style.backgroundColor = '#d3d3d3';
        body.style.backgroundImage = 'none';
        // Carry over the name to the main form
        patientName.value = consentName.value;
        
        updateProgress(); // Make sure this function is defined
    });
    // Function to save selected option respective of question
    function selectOption(questionId, selectedButton){
        const options = document.querySelectorAll(`#${questionId} .option`);

    // Clear previous selections and highlight the selected option
        options.forEach(option => {
            if (option === selectedButton) {
                option.classList.add('selected');  // Highlight selected option
                option.classList.remove('not-selected');  // Remove gray background
                selections[questionId] = option.textContent; // Save selection in dictionary
            } else {
                option.classList.remove('selected');  // Remove highlight
                option.classList.add('not-selected');  // Change background of non-selected
            }
        });
        if (questionId === 'medical_transportation'){
            console.log(selections)
        }
    }

    // Hide all sections initially except for the first question
    const sections = ['help_options', 'second_opinion', 'started_treatment', 'zip_code', 
        'insurance_name','gender_selection', 'ehr_sync', 'ehr_sync_record', 
        'final_questions', 'patientProfiling', 'doctorMatch', 'religiosity', 'immigration_status',
        'ethnicity', 'social_support', 'genetic_testing', 'family_history', 'treatment_approach',
        'doctor_preferences', 'automated_appointment', 'medical_transportation', 'stage_section'];
    sections.forEach(section => {
        document.getElementById(section).style.display = 'none';
    });

    // Handle the questionnaire progression
    document.getElementById('help_today_section').addEventListener('change', function() {
        hideCurrentSection('help_today');
        showNextSection('help_options');
    });

    document.getElementById('help_option').addEventListener('change', function() {
        hideCurrentSection('help_option');
        showNextSection('stage_section');
    });

    document.getElementById('stage_section').addEventListener('change', function(){
        hideCurrentSection('stage_section');
        showNextSection('second_opinion');
    })

    document.querySelectorAll('input[name="second_opinion"]').forEach(function(radio) {
        radio.addEventListener('change', function() {
            hideCurrentSection('second_opinion');
            showNextSection('started_treatment');
        });
    });

    document.querySelectorAll('input[name="started_treatment"]').forEach(function(radio) {
        radio.addEventListener('change', function() {
            hideCurrentSection('started_treatment');
            showNextSection('zip_code');
        });
    });

    document.getElementById('zip_code').addEventListener('change', function() {
        hideCurrentSection('zip_code');
        showNextSection('insurance_name');
    });

    document.getElementById('insurance_name').addEventListener('change', function() {
        hideCurrentSection('insurance_name');
        showNextSection('gender_selection');
    });

    document.getElementById('gender').addEventListener('change', function() {
        hideCurrentSection('gender');
        showNextSection('ehr_sync');
        setTimeout(function () {
            document.querySelector("#ehr_sync p").innerHTML = "Data retrieved. Please verify the information below.";
            showNextSection('ehr_sync_record');
        }, 3000);  // 3000 milliseconds = 3 seconds
    });

    document.querySelectorAll('input[name="confirm_info"]').forEach(function(radio) {
        radio.addEventListener('change', function() {
            hideCurrentSection('ehr_sync_record');
            showNextSection('final_questions');
            setTimeout(function () {
                showNextSection('religiosity');
            }, 1000); 
        });
    });

    document.getElementById('religiosity').addEventListener('change', function(){
        hideCurrentSection('religiosity');
        showNextSection('immigration_status')
    });

    document.getElementById('immigration_status').addEventListener('change', function(){
        hideCurrentSection('immigration_status');
        showNextSection('ethnicity')
    });

    document.getElementById('ethnicity').addEventListener('change', function(){
        hideCurrentSection('ethnicity');
        showNextSection('social_support')
    });

    document.getElementById('social_support').addEventListener('change', function(){
        hideCurrentSection('social_support');
        showNextSection('genetic_testing')
    });

    document.getElementById('genetic_testing').addEventListener('change', function(){
        hideCurrentSection('genetic_testing');
        showNextSection('family_history')
    });

    document.getElementById('family_history').addEventListener('change', function(){
        hideCurrentSection('family_history');
        showNextSection('treatment_approach')
    });

    document.getElementById('treatment_approach').addEventListener('change', function(){
        hideCurrentSection('treatment_approach');
        showNextSection('doctor_preferences')
    });

    document.getElementById('doctor_preferences').addEventListener('change', function() {
        document.getElementById('final_questions').style.display = 'none';
        hideCurrentSection('doctor_preferences');
        showNextSection('patientProfiling');
        setTimeout(function () {
            document.querySelector("#patientProfiling p").innerHTML = "Matching done. Please select the best doctor available.";
            showNextSection('doctorMatch');
        }, 2000);  // 2000 milliseconds = 2 seconds
    });

    document.getElementById('doctorMatch').addEventListener('click', function(){
        hideCurrentSection('doctorMatch');
        showNextSection('automated_appointment');
    });

    document.getElementById('automated_appointment').addEventListener('click', function(){
        hideCurrentSection('automated_appointment');
        showNextSection('medical_transportation');
    });

    // Function to show the next section
    function showNextSection(sectionId) {
        document.getElementById(sectionId).style.display = 'block';
        smoothScroll('#' + sectionId);
    }

    // Function to hide the current section
    function hideCurrentSection(sectionId){
        //document.getElementById(sectionId).parentElement.style.display = 'none';
        //document.getElementById(sectionId).style.display = 'none';
    }

    // // Function to save selected option respective of question
    // function selectOption(questionId, selectedButton){
    //     const options = document.querySelectorAll(`#${questionId} .option`);

    // // Clear previous selections and highlight the selected option
    //     options.forEach(option => {
    //         if (option === selectedButton) {
    //             option.classList.add('selected');  // Highlight selected option
    //             option.classList.remove('not-selected');  // Remove gray background
    //             selections[questionId] = option.textContent; // Save selection in dictionary
    //         } else {
    //             option.classList.remove('selected');  // Remove highlight
    //             option.classList.add('not-selected');  // Change background of non-selected
    //         }
    //     });
    //     if (questionId === 'medical_transportation'){
    //         console.log(selections)
    //     }
    // }

    document.querySelector("#patientForm").addEventListener('formdata', (e) => {

        const formData = e.formData; 
        //console.log(Object.fromEntries(formData.entries()));
        formData.append('name', document.getElementById('consentName').value);
        let dob = new Date(document.getElementById('consentDOB').value);
        let age = ((Date.now() - dob) / (31557600000));
        formData.append('age', parseInt(age));
        console.log(Object.fromEntries(formData.entries()));
      });
    // Form validation before submission
    patientForm.addEventListener('submit', function(event) {
        let isValid = true;
        // let entries = Object.fromEntries(new FormData(patientForm).entries());
        // console.log(entries);
        // Validate required fields
        const requiredFields = ['name', 'age', 'stage', 'location', 'family_history', 'genetic_testing'];
        requiredFields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (!validateInput(field, `Please fill out the ${field.name.replace('_', ' ')} field.`)) {
                isValid = false;
            }
        });

        // Validate age
        const age = document.getElementById('age');
        if (!validateAge(age, 'Please enter a valid age between 0 and 120.')) {
            isValid = false;
        }

        // Validate social support radio buttons
        const socialSupport = document.querySelector('input[name="social_support"]:checked');
        if (!socialSupport) {
            alert('Please select whether you need social support.');
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault(); // Prevent form submission if validation fails
        } else {
            if (!confirm('Are you sure you want to submit the form?')) {
                event.preventDefault();
            }
        }
    });

    // Function to validate input fields
    function validateInput(input, errorMessage) {
        if (input.value.trim() === '') {
            alert(errorMessage);
            input.focus();
            return false;
        }
        return true;
    }

    // Function to validate age input
    function validateAge(input, errorMessage) {
        const age = parseInt(input.value);
        if (isNaN(age) || age < 0 || age > 120) {
            alert(errorMessage);
            input.focus();
            return false;
        }
        return true;
    }

    // Add smooth scrolling for better UX when validation fails
    function smoothScroll(target) {
        const element = document.querySelector(target);
        window.scrollTo({
            top: element.offsetTop - 20,
            behavior: 'smooth'
        });
    }

    // Enhance form interactivity
    const formFields = document.querySelectorAll('input, select, textarea');
    formFields.forEach(field => {
        field.addEventListener('focus', function() {
            this.parentElement.classList.add('active');
        });

        field.addEventListener('blur', function() {
            if (this.value.trim() === '') {
                this.parentElement.classList.remove('active');
            }
        });
    });

    // Optional: Add a confirmation before form submission
    // patientForm.addEventListener('submit', function(event) {
    //     if (!confirm('Are you sure you want to submit the form?')) {
    //         event.preventDefault();
    //     }
    // });
});