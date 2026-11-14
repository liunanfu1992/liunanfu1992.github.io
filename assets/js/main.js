/* Theme and section navigation. Content remains accessible without JavaScript. */
(() => {
  const root = document.documentElement;
  const button = document.getElementById('theme');
  const currentTheme = () => root.dataset.theme === 'light' ? 'light' : 'dark';
  function updateThemeLabel() {
    if (!button) return;
    const dark = currentTheme() === 'dark';
    const label = dark ? 'Switch to light mode' : 'Switch to dark mode';
    button.dataset.mode = dark ? 'dark' : 'light';
    button.setAttribute('aria-label', label);
    button.title = label;
  }
  if (button) {
    button.hidden = false;
    button.addEventListener('click', () => {
      root.dataset.theme = currentTheme() === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('theme', root.dataset.theme); } catch (error) { /* Optional persistence. */ }
      updateThemeLabel();
    });
    updateThemeLabel();
  }

  const links = [...document.querySelectorAll('.toc a')];
  const sections = [...document.querySelectorAll('main section')];
  function updateSection() {
    if (!sections.length) return;
    let active = sections[0];
    const marker = Math.min(innerHeight * 0.25, 180);
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= marker) active = section;
    }
    if (innerHeight + scrollY >= document.documentElement.scrollHeight - 4) {
      active = sections[sections.length - 1];
    }
    for (const link of links) {
      const selected = link.hash === '#' + active.id;
      link.classList.toggle('cur', selected);
      if (selected) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    }
  }
  let scheduled = false;
  function scheduleUpdate() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(() => { updateSection(); scheduled = false; });
  }
  addEventListener('scroll', scheduleUpdate, { passive: true });
  addEventListener('resize', scheduleUpdate);
  addEventListener('hashchange', scheduleUpdate);
  addEventListener('load', updateSection);
  updateSection();
})();
