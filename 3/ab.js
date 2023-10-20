// Define your colors and other variables as before

let notoggle = true;

// const handleOnClick1 = (x, y) => {
//     notoggle = !notoggle;
//     const columns = Math.floor(document.body.clientWidth / 50);
//     const rows = Math.floor(document.body.clientHeight / 50);

//     // Calculate the grid number based on mouse coordinates
//     const colNumber = Math.floor(x / 50); // Assuming each tile is 50px wide
//     const rowNumber = Math.floor(y / 50); // Assuming each tile is 50px tall

//     const gridNumber = colNumber + rowNumber * columns;

//     // console.log(`Mouse clicked on grid tile number: ${gridNumber}`);

//     anime({
//         targets: '.abtile',
//         opacity: notoggle ? 0 : 1,
//         backgroundColor: "rgb(255, 255, 255)",
//         delay: anime.stagger(50, { grid: [columns, rows], from: gridNumber })
//     });

//     const ple = document.getElementById("ple");
//     anime({
//         targets: ple,
//         opacity: notoggle ? 1 : 0,
//         backgroundColor: "rgb(0, 0, 0)",
//         color: "black",
//         delay: anime.stagger(50, { grid: [columns, rows], from: gridNumber })
//     });
// };


const hndleOnClick1 = (event) => {
    notoggle = !notoggle;
    const x = event.clientX; // Mouse X coordinate
    const y = event.clientY;
    const columns = Math.floor(document.body.clientWidth / 50);
    const rows = Math.floor(document.body.clientHeight / 50);

    // Calculate the grid number based on mouse coordinates
    const colNumber = Math.floor(x / 50); // Assuming each tile is 50px wide
    const rowNumber = Math.floor(y / 50); // Assuming each tile is 50px tall

    const gridNumber = colNumber + rowNumber * columns;

    // console.log(`Mouse clicked on grid tile number: ${gridNumber}`);

    anime({
        targets: '.abtile',
        opacity: notoggle ? 0 : 1,
        backgroundColor: "rgb(0, 0, 0)",
        delay: anime.stagger(50, { grid: [columns, rows], from: gridNumber })
    });

    const ple = document.getElementById("ple");
    anime({
        targets: ple,
        opacity: notoggle ? 1 : 0,
        // backgroundColor: "rgb(0, 0, 0)",
        color: "black",
        delay: anime.stagger(50, { grid: [columns, rows], from: gridNumber })
    });
    const plev = document.getElementById("plve");
    anime({
        targets: plev,
        opacity: notoggle ? 0 : 1,
        // backgroundColor: "rgb(0, 0, 0)",
        color: "white",
        delay: anime.stagger(50, { grid: [columns, rows], from: gridNumber })
    });
};


const createTile1 = (index) => {
    const abtile = document.createElement("div");
    abtile.classList.add("abtile");
    // abtile.onclick = (event) => {
    //     const x = event.clientX; // Mouse X coordinate
    //     const y = event.clientY; // Mouse Y coordinate
    //     handleOnClick1(x, y);
    // };
    return abtile;
};

const createTiles1 = (quantity) => {
    const wrapper1 = document.getElementById("atiles");
    Array.from(Array(quantity)).forEach((_, index) => {
        wrapper1.appendChild(createTile1(index));
    });
};

const clearAndGenerateGrid1 = () => {
    const wrapper1 = document.getElementById("atiles");
    wrapper1.innerHTML = "";

    const col = Math.floor(document.body.clientWidth / 50);
    const row = Math.floor(document.body.clientHeight / 50);

    wrapper1.style.setProperty("--col", col);
    wrapper1.style.setProperty("--row", row);

    const totalTiles = col * row;
    createTiles1(totalTiles);
};

window.addEventListener("DOMContentLoaded", clearAndGenerateGrid1);
window.addEventListener("resize", clearAndGenerateGrid1);
