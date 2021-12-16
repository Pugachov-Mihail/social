<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <register-form />
  </div>
</template>

<script>
// @ is an alias to /src
import RegisterForm from "../components/RegisterForm.vue";

export default {
  name: "Home",
  components: {
    RegisterForm,
  },
};
</script>
