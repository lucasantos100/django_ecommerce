// Função para carregar dados do localStorage
function loadProfile() {
    // Carregar a imagem de perfil
    const savedImage = localStorage.getItem("profileImage");
    const profileImage = document.getElementById("profileImage");

    if (savedImage) {
        profileImage.src = savedImage;  // Define a imagem salva no perfil
    }

    // Carregar a descrição
    const savedBio = localStorage.getItem("bio");
    const bioTextarea = document.getElementById("bio");

    if (savedBio) {
        bioTextarea.value = savedBio;  // Define a descrição salva
    }
}

// Função para salvar dados no localStorage
function saveProfile() {
    const bioTextarea = document.getElementById("bio");
    const profileImage = document.getElementById("profileImage");

    // Salvar a descrição no localStorage
    localStorage.setItem("bio", bioTextarea.value);

    // Salvar a imagem no localStorage como uma URL de imagem base64
    const imageData = profileImage.src;
    localStorage.setItem("profileImage", imageData);
}

// Função para permitir alteração de imagem
function handleImageChange(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onloadend = function () {
        const profileImage = document.getElementById("profileImage");
        profileImage.src = reader.result;

        // Salvar a nova imagem no localStorage
        localStorage.setItem("profileImage", reader.result);
    };

    if (file) {
        reader.readAsDataURL(file); // Converter a imagem para base64
    }
}

// Função para alternar entre os modos de "editar" e "salvar"
function toggleEditMode() {
    const bioTextarea = document.getElementById("bio");
    const editButton = document.getElementById("editButton");
    const saveButton = document.getElementById("saveButton");

    if (editButton.style.display === "none") {
        bioTextarea.readOnly = true;
        editButton.style.display = "inline-block";
        saveButton.style.display = "none";
    } else {
        bioTextarea.readOnly = false;
        editButton.style.display = "none";
        saveButton.style.display = "inline-block";
    }
}

// Eventos
document.getElementById("imageInput").addEventListener("change", handleImageChange);
document.getElementById("saveButton").addEventListener("click", () => {
    saveProfile();
    toggleEditMode();
});
document.getElementById("editButton").addEventListener("click", toggleEditMode);

// Carregar perfil ao iniciar a página
loadProfile();
