    $(document).ready(function() {
        function cookieController() {
            // Cookie setting scripts in here
        }   

    var userLang = navigator.language || navigator.userLanguage;
    var xLang = userLang.split('-')[0]; // language code

      if(xLang == 'es') {
        $.cookiesDirective({
            privacyPolicyUri: 'privacy-policy-es.html',
            inlineAction: true,
            explicitConsent: false,
            duration: 60, // display time in seconds
            impliedSubmitText: 'Entendido',
            fontFamily: 'Roboto', // font style for disclosure panel
            linkColor: '#26a69a', // link color in disclosure panel
            message: 'Utilizamos cookies propias y de terceros para mejorar nuestro servicio, recoger información estadística sobre su navegación y mostrarle publicidad relacionada con sus preferencias. Si continúa navegando, consideramos que acepta su uso. ',
            impliedDisclosureText: 'Más información en nuestra ',
            privacyPolicyLinkText: 'politica de privacidad',
            explicitCookieAcceptanceLabel: '',
            scriptWrapper: cookieController
        });
      }
      else {
        $.cookiesDirective({
            privacyPolicyUri: 'privacy-policy-en.html',
            inlineAction: true,
            explicitConsent: false,
            duration: 60, // display time in seconds
            impliedSubmitText: 'I understand',
            fontFamily: 'Roboto', // font style for disclosure panel
            linkColor: '#26a69a', // link color in disclosure panel
            message: 'We use our own and third party cookies to improve our service, collect statistical information about your browsing and show related advertising to your preferences. If you continue browsing this website, we will consider you accepting its use. ', // customise the disclosure message
            explicitCookieAcceptanceLabel: '',
            impliedDisclosureText: 'More information in our ',
            privacyPolicyLinkText: 'privacy policy',
            scriptWrapper: cookieController
        });
      }

    });