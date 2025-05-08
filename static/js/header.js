document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('header');
    if (!header) return;

    let didScroll = false;
    let lastScrollTop = 0;
    const delta = 10;
    const navbarHeight = header.offsetHeight;
    let bodyElement;

    // Функция для проверки наличия body.active
    function checkBodyActive() {
        bodyElement = document.querySelector('body.active');
        if (bodyElement) {
            bodyElement.addEventListener('scroll', () => {
                didScroll = true;
            });
            return true;
        }
        return false;
    }

    const checkInterval = setInterval(() => {
        if (checkBodyActive()) {
            clearInterval(checkInterval);
        }
    }, 100);

    setInterval(() => {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 100);

    function hasScrolled() {
        if (!bodyElement) return;

        const st = bodyElement.scrollTop;
        
        // Проверяем, изменился ли скролл больше, чем delta
        if (Math.abs(lastScrollTop - st) <= delta) return;

        // Скрыть хедер при прокрутке вниз
        if (st > lastScrollTop && st > navbarHeight) {
            header.classList.remove('nav-down');
            header.classList.add('nav-up');
        } 
        // Показать хедер при прокрутке вверх
        else {
            if (st + bodyElement.clientHeight < bodyElement.scrollHeight) {
                header.classList.remove('nav-up');
                header.classList.add('nav-down');
            }
        }
        
        lastScrollTop = st;
    }
});
