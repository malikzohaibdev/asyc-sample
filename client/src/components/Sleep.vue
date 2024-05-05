<script setup>
import { ref } from "vue";
const props = defineProps(["elapsedTime"])

</script>
<template>

    <h3>{{ props.elapsedTime }}</h3>

</template>
<style></style>