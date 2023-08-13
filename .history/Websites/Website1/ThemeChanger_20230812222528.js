const themeToggle = document.getElementById("theme-toggle");
const themeLink = document.getElementById("theme-link");
let currentTheme = "Theme1";

themeToggle.addEventListener("click", () => {
    currentTheme = currentTheme === "Dark" ? "Design" : "Theme1";
    themeLink.href = `Themes/${currentTheme}.css`;
});
