// const colors = [...]; // You can uncomment this if you want to use colors

let toggle = false;

const handleOnClick = (tile, index) => {
  toggle = !toggle;
  const columns = parseInt(getComputedStyle(tile).getPropertyValue("--col"));
  const rows = parseInt(getComputedStyle(tile).getPropertyValue("--row"));

  anime({
    targets: tile, // Target the clicked tile
    opacity: toggle ? 0 : 1, // Toggle opacity
    delay: anime.stagger(50, { grid: [columns, rows], from: index })
  });
};

const createTile = (index) => {
    const tile = document.createElement("div");
    tile.classList.add("tile");
    tile.onclick = () => handleOnClick(tile, index);
    return tile;
};

const createTiles = (quantity) => {
    const wrapper = document.getElementById("tiles");
    Array.from(Array(quantity)).forEach((_, index) => {
        wrapper.appendChild(createTile(index));
    });
};

const clearAndGenerateGrid = () => {
    const wrapper = document.getElementById("tiles");
    wrapper.innerHTML = "";

    const col = Math.floor(document.body.clientWidth / 50);
    const row = Math.floor(document.body.clientHeight / 50);

    wrapper.style.setProperty("--col", col);
    wrapper.style.setProperty("--row", row);

    const totalTiles = col * row;
    createTiles(totalTiles);
};

window.addEventListener("DOMContentLoaded", clearAndGenerateGrid);
window.addEventListener("resize", clearAndGenerateGrid);
