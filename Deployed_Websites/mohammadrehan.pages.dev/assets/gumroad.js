{
  const script = document.createElement("script");
  script.src = "https://assets.gumroad.com/js/gumroad-bundle.js";
  script.charset = "utf-8";
  document.head.appendChild(script);
    document.head.insertAdjacentHTML('beforeend', '<link rel="stylesheet" href="https://assets.gumroad.com/vite/assets/entrypoints/overlay-BHH_eIA6.css" />');

    const loaderScript = document.querySelector("script[src*='/js/gumroad.js']");
    loaderScript.dataset.stylesUrl = "https://assets.gumroad.com/vite/assets/entrypoints/design-DXLDXIo0.css";
}
