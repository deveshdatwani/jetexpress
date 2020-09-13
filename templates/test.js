let btnAdd = document.getElementById('button');
let table = document.getElementsByTagName('table')[0];

btnAdd.addEventListener('click', () => {

    let template =  " <tr> <td>.</td> <td>.</td> <td>.</td> <td>.</td> <td>.</td> </tr>";
    table.innerHTML += template;
});