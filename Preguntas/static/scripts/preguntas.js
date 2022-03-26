url = window.location.href

url = url.toString()

let materia = ''
let incio = false

for (let i = 0 ; i<= url.length -1 ;i++) {
    if (incio){
        materia = materia + url[i]
    }
    if (url[i] === '?') {
        incio = true
    }
    
}


console.log(materia)

let idmateria = 0

if (materia=="Matem%C3%A1ticas"){
    idmateria = "1" 
}
else if (materia=="F%C3%ADsica"){
    idmateria = "2" 
}
else if (materia=="Biolog%C3%ADa"){
    idmateria = "3" 
}
else if (materia=="Qu%C3%ADmica"){
    idmateria = "4"
}
else{
    idmateria = "5"
}

let opcion, copciones

function shuffleArray(inputArray){
    inputArray.sort(()=> Math.random() - 0.5);
}

const validacion = async (id,valor,ids) =>{
    let listaid = []
    for (i=0;i<ids.length;i=i+2){
        listaid.push(ids[i])
    }
    seleccionada = document.getElementById(id)
    correcta = document.getElementById(valor)
    if(id==valor){
        seleccionada.style.backgroundColor = 'lightgreen';
    }
    else{
        seleccionada.style.backgroundColor = 'lightcoral';
        correcta.style.backgroundColor = 'lightgreen';
    }
}

let val
let ids = []

let idp = []

const boton = async () => {
    copciones = document.getElementById("opciones")
    copciones.innerHTML= ""
    aleatoria()
}

const aleatoria = async () =>{
    idp = []
    let urlo = "/preguntas/?materia_p=" + idmateria
    const pŕeguntaslp = await fetch(urlo);
    const preguntasl = await pŕeguntaslp.json()
    preguntasl.forEach(element =>{
        idp.push(element.id)
    })
    pregunta()
};

const pregunta = async () =>{
    ids = []
    let urlp = "/preguntas/?materia_p=" + idmateria 
    const preguntasp = await fetch(urlp);
    const preguntas = await preguntasp.json()
    cpregunta = document.getElementById("pregunta")
    let rand = Math.floor(Math.random()*idp.length);
    console.log(rand)
    cpregunta.innerHTML = preguntas[rand].pregunta
    if (idmateria == "1"){
        cpregunta.style.backgroundColor = 'rgba(255, 0, 0, 0.719)';
        cpregunta.style.color = 'white';
    } 
    else if (idmateria == "2"){
        cpregunta.style.backgroundColor = 'rgba(74, 195, 243, 0.719)';
    }
    else if (idmateria == "3"){
        cpregunta.style.backgroundColor = 'rgba(1, 68, 1, 0.719)';
        cpregunta.style.color = 'white';
    }
    else if (idmateria == "4"){
        cpregunta.style.backgroundColor = 'rgb(0, 14, 58)';
        cpregunta.style.color = 'white';
    }
    else if (idmateria == "5"){
        cpregunta.style.backgroundColor = 'white';
    }
    let urlo = "/opciones/?pregunta_o=" + preguntas[rand].id
    const opcionesp = await fetch(urlo);
    const opciones = await opcionesp.json()
    copciones = document.getElementById("opciones")
    shuffleArray(opciones)
    opciones.forEach(element => {
        ids.push(element.id)
        if(element.correcta==true){
            val = element.id
        }
    });
    opciones.forEach(element => {
        opcion = document.createElement('div')
        opcion.classList.add('Opcionf')
        opcion.setAttribute("id", ""+element.id+"");
        opcion.innerHTML = element.opcion
        opcion.setAttribute("onclick", "validacion('"+element.id+"','"+val+"','"+ids+"')");
        copciones.appendChild(opcion)
    });
    console.log(ids)
}

aleatoria()


