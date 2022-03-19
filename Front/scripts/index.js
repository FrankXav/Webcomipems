function irpreguntas(materia) {
    let ruta = 'http://127.0.0.1:5500/Front/preguntas.html'+'?'+materia
    window.location = ruta
}


const listmaterias = async () => {
    const materiasi = await fetch('http://127.0.0.1:8000/listmaterias/');
    const materias = await materiasi.json()
    conteiner = document.getElementById('materias')
    console.log(materias)
    materias.forEach(element => {
        opciones = document.createElement('div')
        opciones.setAttribute("id", element.materia);
        opciones.setAttribute("onclick", "irpreguntas('"+element.materia+"')");
        opciones.classList.add('Opcion')
        if (element.materia == 'Matemáticas'){
            opciones.style.backgroundColor = 'rgba(255, 0, 0, 0.719)';
            opciones.style.color = 'white';
        } 
        else if (element.materia == 'Física'){
            opciones.style.backgroundColor = 'rgba(74, 195, 243, 0.719)';
        }
        else if (element.materia == 'Biología'){
            opciones.style.backgroundColor = 'rgba(1, 68, 1, 0.719)';
            opciones.style.color = 'white';
        }
        else if (element.materia == 'Química'){
            opciones.style.backgroundColor = 'rgb(0, 14, 58)';
            opciones.style.color = 'white';
        }
        else if (element.materia == 'Aleatorio'){
            opciones.style.backgroundColor = 'white';
        }
        nombrem = document.createElement('div')
        nombrem.classList.add('Nombre')
        nombrem.innerHTML = element.materia
        console.log(element.materia)
        opciones.appendChild(nombrem)
        conteiner.appendChild(opciones)
    });
}

listmaterias()

