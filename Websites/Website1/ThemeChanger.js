const themeToggle = document.getElementById("theme-toggle");
const themeLink = document.getElementById("theme-link");
let currentTheme = "Dark";

themeToggle.addEventListener("click", () => {
    if (currentTheme === "Dark") {
        currentTheme = "Light";
    } else if (currentTheme === "Light") {
        currentTheme = "Design";
    } else if (currentTheme === "Design") {
        currentTheme = "Galactic";
    }
    else {
        currentTheme = "Dark";
    }
    themeLink.href = `Themes/${currentTheme}.css`;
});
