const themeToggle = document.getElementById("theme-toggle");
const themeLink = document.getElementById("theme-link");
let currentTheme = "Theme1";

themeToggle.addEventListener("click", () => {
    currentTheme = currentTheme === "Theme1" ? "Theme2" : "Theme1";
  themeLink.href = `Themes/${currentTheme}.css`;
});
