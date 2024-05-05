<script setup>
import { ref } from "vue";
const props = defineProps(["elapsedTime"])

</script>
<template>

    <h3 class="text-3xl">{{ props.elapsedTime }} Seconds</h3>

</template>
<style></style>