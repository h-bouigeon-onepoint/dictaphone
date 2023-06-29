// Add loading animation when buttons are clicked
const btns = document.querySelectorAll('button');
btns.forEach((items) => {
    items.addEventListener('click', (evt) => {
        evt.target.classList.add('activeLoading');
    })
})

// Allow switch for different meeting report selector 
// (select html element displays when there is more than 4 meeting reports to display)
const meetingReportSelector = document.getElementById('meetingReportSelector');
if (meetingReportSelector) {
    meetingReportSelector.addEventListener('change', (element) => {
        const selected_value = element.target.value;
        const tabContents = document.getElementsByClassName("tab-content");
        for (let i = 0; i < tabContents.length; i++) {
            tabContents[i].style.display = "none";
        }

        const tabButtons = document.getElementsByClassName("tab-btn");
        for (let i = 0; i < tabButtons.length; i++) {
            tabButtons[i].className = tabButtons[i].className.replace(" active", " ");
        }

        const meetingReportSelected = document.getElementById("meeting_report_" + selected_value);
        meetingReportSelected.style.display = "block";
        meetingReportSelected.className += " active";
    });

    // Create an event to display first meeting report
    var eventToDisplayFirstElement = new CustomEvent("change", { "element": 0 });
    // Dispatch/Trigger/Fire the event (no matter the element given)
    meetingReportSelector.dispatchEvent(eventToDisplayFirstElement);
}

// Allow switch for different tabs button
function openReport(evt, reportId) {
    const tabContents = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
    }

    const tabButtons = document.getElementsByClassName("tab-btn");
    for (let i = 0; i < tabButtons.length; i++) {
        tabButtons[i].className = tabButtons[i].className.replace(" active", " ");
    }

    document.getElementById(reportId).style.display = "block";
    evt.currentTarget.className += " active";
}
// Click on first element to display first meeting report
document.getElementsByClassName("tab-btn")[0].click();