const menuButton = document.querySelector('.menu-button');
const navigation = document.querySelector('#site-nav');
const menuLabel = menuButton?.querySelector('.sr-only');

function setMenu(open) {
  if (!menuButton) return;
  menuButton.setAttribute('aria-expanded', String(open));
  document.body.classList.toggle('menu-open', open);
  menuLabel.textContent = open ? 'Close navigation' : 'Open navigation';
}
menuButton?.addEventListener('click', () => {
  const wasOpen = menuButton.getAttribute('aria-expanded') === 'true';
  setMenu(!wasOpen);
  if (wasOpen) menuButton.focus();
});
navigation?.addEventListener('click', (event) => { if (event.target.matches('a')) setMenu(false); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') { setMenu(false); menuButton.focus(); } });
window.addEventListener('resize', () => { if (window.innerWidth > 760) setMenu(false); });

document.querySelectorAll('[data-details]').forEach((button) => {
  button.addEventListener('click', () => {
    const container = document.getElementById(button.dataset.target);
    const shouldOpen = button.dataset.details === 'expand';
    container.querySelectorAll('details').forEach((details) => { details.open = shouldOpen; });
  });
});
