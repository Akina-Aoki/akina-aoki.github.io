const menuButton = document.querySelector('.menu-button');
const navigation = document.querySelector('#site-nav');
const menuLabel = menuButton.querySelector('.sr-only');

function setMenu(open) {
  menuButton.setAttribute('aria-expanded', String(open));
  document.body.classList.toggle('menu-open', open);
  menuLabel.textContent = open ? 'Close navigation' : 'Open navigation';
}
menuButton.addEventListener('click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true'));
navigation.addEventListener('click', (event) => { if (event.target.matches('a')) setMenu(false); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') { setMenu(false); menuButton.focus(); } });
window.addEventListener('resize', () => { if (window.innerWidth > 760) setMenu(false); });

document.querySelectorAll('[data-details]').forEach((button) => {
  button.addEventListener('click', () => {
    const container = document.getElementById(button.dataset.target);
    const shouldOpen = button.dataset.details === 'expand';
    container.querySelectorAll('details').forEach((details) => { details.open = shouldOpen; });
  });
});

const navLinks = [...navigation.querySelectorAll('a')];
const sections = navLinks.map((link) => document.querySelector(link.hash)).filter(Boolean);
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.filter((entry) => entry.isIntersecting).forEach((entry) => {
      navLinks.forEach((link) => link.removeAttribute('aria-current'));
      navigation.querySelector(`a[href="#${entry.target.id}"]`)?.setAttribute('aria-current', 'location');
    });
  }, { rootMargin: '-25% 0px -65%' });
  sections.forEach((section) => observer.observe(section));
}
