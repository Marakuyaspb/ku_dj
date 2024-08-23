const tabs = document.querySelectorAll('[data-id]');
let activeTab = tabs[0]; 

tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
        activeTab.classList.remove('active_choice_tab');
        tab.classList.add('active_choice_tab');
        activeTab = tab;
    });
});
