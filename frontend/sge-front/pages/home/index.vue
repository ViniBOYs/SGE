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
        <h1>Minha Tela Home!!!</h1>
        <button @click="logout" class="customButtonOut" >SAIR</button>
    </div>
</template>

<style lang="scss">

</style>