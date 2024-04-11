<script setup lang="ts">

const { signOut } = useAuth()

definePageMeta({
    middleware: 'auth'
})

const logout = () => {
    signOut({redirect: false})
    .then(()=>{
        console.log("Successfully logged out");
        navigateTo("/");
    })
    .catch((error)=>{
        console.log("Error when trying to execute logout: ",error);
    })
}

</script>

<template>
    <div class="teste">
        <section class="top_menu">
            <div class="tp_left">
                <h3>1 - Vamos</h3>
                <h3>2 - Fazer</h3>
            </div>
            <div class="tp_right">
                <h3>3 - Aquele</h3>
                <h3 class="brinquedo">4 - Teste</h3>
            </div>
        </section>
        <h1>Minha Tela Home!!!</h1>
        <button @click="logout" class="customButtonOut" >SAIR</button>
        <span @click="logout" class="btn">SAIR</span>
    </div>

    <div class="data-container">

    </div>

</template>

<style lang="scss">

.top_menu{
    width: 100%;
    height: 4vw;
    display: flex;
    flex-direction: row;
    // align-items:center;
    background-color: magenta;
    justify-content:space-between;
}

.tp_right{
    display: flex;
    flex-direction: row;
    justify-content: end;
    width: 47.5%;
    background-color: purple;        
}

.tp_left{
    display: flex;
    flex-direction: row;
    justify-content: start;
    width: 47.5%;
    background-color: red;
}

.brinquedo{
    transition: all 2s;
    &:hover{
        color: white;
        font-size: 20px;
    }
}

</style>