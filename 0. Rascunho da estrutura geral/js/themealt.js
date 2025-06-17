function themeAlt(){    
    var tema = document.querySelector('html').getAttribute('data-bs-theme')
    if(tema === 'light'){
        document.querySelector('html').setAttribute('data-bs-theme', 'dark');


    } else{
        document.querySelector('html').setAttribute('data-bs-theme', 'light');
    }
}