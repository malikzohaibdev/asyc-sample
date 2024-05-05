<script setup>
import { ref } from "vue"
import Sleep from "./components/Sleep.vue"
const execTime = ref(null)
const getRequest = async function () {
    try {
        const response = await fetch("http://localhost:8000/async")
        const data = await response.json()
        console.log(data)
    } catch (error) {
        console.log(error)
    }

}
</script>
<template>

    <Sleep :v-if="execTime" :elapsed-time="execTime"></Sleep>

    <button @click="getRequest">Send Request</button>
</template>

<style scoped></style>
