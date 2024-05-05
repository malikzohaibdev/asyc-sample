<script setup>
import { ref } from "vue"
import Sleep from "./components/Sleep.vue"
const execTime = ref(0)
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

    <div>
        <div v-if="loading">
            Loading....
        </div>
        <div v-else>
            <Sleep :elapsed-time="execTime"></Sleep>
        </div>
    </div>

    <button @click="getRequest">Send Request</button>
</template>

<style scoped></style>
