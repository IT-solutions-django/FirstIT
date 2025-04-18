let lenis;


const contentElements = [...document.querySelectorAll('.content--sticky.card')];
const totalContentElements = contentElements.length;

console.log(contentElements)

const initSmoothScrolling = () => {
	lenis = new Lenis({
		lerp: 0.1, 
		smoothWheel: false
	});

	lenis.on('scroll', () => ScrollTrigger.update());

	// Define a function to run at each animation frame
	const scrollFn = (time) => {
		lenis.raf(time); // Run Lenis' requestAnimationFrame method
		requestAnimationFrame(scrollFn); 
	};
	// Start the animation frame loop
	requestAnimationFrame(scrollFn);
};

// Function to handle scroll-triggered animations
const scroll = () => {
    const fixedMenu = document.querySelector('.fixed-menu');

    gsap.timeline({
        scrollTrigger: {
            trigger: '.services-section',
            start: 'top+=10 top',
            end: 'bottom-=100 top', 
            scrub: true,
        }
    });
    
    contentElements.forEach((el, position) => {

        const isLast = position === totalContentElements-1;

        const currentIndex = el.dataset.tabId;

        console.log(currentIndex)
        
        gsap.timeline({
            scrollTrigger: {
                trigger: el,
                start: 'center center',
                end: '+=100%',
                scrub: true, 
                onEnter: () => {
                    setActiveCard()
                },
            }
        })
        .to(el, {
            ease: 'none',
            scale: 0.6,
            opacity: 0,
            yPercent: isLast ? 0 : 0,  
            rotationY: 30, 
            transformOrigin: 'center',
            z: 200,  
            perspective: 800,
            zIndex: position, 
            willChange: 'transform'
        }, 0);
    });

};

// Initialization function
const init = () => {
    initSmoothScrolling(); 
    scroll(); 
};


document.addEventListener('DOMContentLoaded', () => {
    init();
});


// function setActiveCard(index) {
//     const cards = document.querySelectorAll('.tab');
//     cards.forEach((card) => {
//         card.classList.remove('active'); 
//     });
//     const activeCard = cards.querySelector(`tab[data-tab-id="${index}"]`);
//     activeCard.classList.add('active');
// }



window.addEventListener('scroll', function() {
    const container = this.document.querySelector('.container.main.home'); 
    const menu = this.document.querySelector('.fixed-menu'); 
    const heading = this.document.querySelector('.section__heading '); 

    const cards = this.document.querySelectorAll('.content--sticky')
    const lastCard = cards[cards.length - 1];

    const containerRect = container.getBoundingClientRect();
    const menuRect = menu.getBoundingClientRect();
    const headingRect = heading.getBoundingClientRect();
    const lastCardRect = lastCard.getBoundingClientRect();

    if (containerRect.top < 0) {
        if (lastCardRect.bottom - 201 <= menuRect.height) {
            menu.style.position = 'absolute';
            menu.style.top = 'auto';
            menu.style.bottom = '0';
        } else {
            menu.style.position = 'fixed';
            menu.style.top = '201px';
            menu.style.bottom = 'auto';
        }
    } 
    else {
        menu.style.position = 'absolute';
        menu.style.top = '101px'; 
    }

    if (containerRect.top < 0) {
        if (lastCardRect.bottom <= headingRect.height + 580 + 60) {
            heading.style.position = 'absolute';
            heading.style.bottom = (580 + 60) + 'px';
            heading.style.top = 'auto';
            heading.style.right = 'calc((1400px - ' + heading.clientWidth + 'px) / 2)';
            heading.style.opacity = '0'
        } else {
            heading.style.opacity = '1'
            heading.style.position = 'fixed';
            heading.style.top = '100px';
            heading.style.right = 'calc((100vw - 1400px) / 2 + (1400px - ' + heading.clientWidth + 'px) / 2 - 10px)';
        }
    } else {
        heading.style.position = 'relative';
        heading.style.top = '0px';
        heading.style.right = '0px';
    }
});

