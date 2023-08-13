const themeToggle = document.getElementById("theme-toggle");
const themeLink = document.getElementById("theme-link");
let currentTheme = "Dark";

themeToggle.addEventListener("click", () => {
    currentTheme = currentTheme === "Dark" ? "Design" : "Dark";
    themeLink.href = `Themes/${currentTheme}.css`;
});
