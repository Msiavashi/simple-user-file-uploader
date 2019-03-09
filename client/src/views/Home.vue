<template>
    <login></login>
</template>

<script>
import Login from "@/components/Login";
export default {
  props: {
    source: String
  },
  components: {
      Login
  }
}
</script>