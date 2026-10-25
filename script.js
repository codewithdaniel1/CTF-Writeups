document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = new Date().getFullYear();
});

document.querySelectorAll("[data-back-to-ctf]").forEach((link) => {
  link.addEventListener("click", (event) => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || !document.referrer || history.length < 2) {
      return;
    }

    const previous = new URL(document.referrer);
    const listing = new URL(link.href);
    if (previous.origin === listing.origin && previous.pathname === listing.pathname) {
      event.preventDefault();
      history.back();
    }
  });
});
