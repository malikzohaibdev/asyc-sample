<script setup>
import { ref } from "vue"
import Sleep from "./components/Sleep.vue"
const execTime = ref(null)
const loading = ref(false)
const getRequest = async function () {
    try {
        loading.value = true
        const response = await fetch("http://localhost:8000/async")
        const data = await response.json()
        execTime.value = data.elapsed
        loading.value = false
    } catch (error) {
        console.log(error)
    }

}
</script>
<template>

    <h1>Elapsed Time</h1>
    <div v-if="loading">
        Loading....
    </div>
    <Sleep v-else :elapsed-time="execTime"></Sleep>
    <button @click="getRequest">Send Request</button>
</template>

<style scoped></style>
