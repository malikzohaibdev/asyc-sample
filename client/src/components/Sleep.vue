<script setup>
import { ref } from "vue";
const props = defineProps(["elapsedTime"])

</script>
<template>
    <div>
        <h3>{{ props.elapsedTime }}</h3>
    </div>
</template>
<style></style>