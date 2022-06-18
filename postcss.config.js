const path = require("path");

module.exports = () => ({
  plugins: [
    require("tailwindcss")(path.resolve(__dirname, "tailwind.config.js")),
    require("autoprefixer"),
    process.env.FLASK_ENV === "production" &&
      require("@fullhuman/postcss-purgecss")({
        content: [path.resolve(__dirname, "app/templates/*.html")],
        defaultExtractor: (content) => content.match(/[A-Za-z0-9-_:/]+/g) || [],
      }),
  ],
});
