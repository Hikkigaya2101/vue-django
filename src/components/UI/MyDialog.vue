<template>
<div class = "dialog" v-if="show" @click="hideDialog">
<div @click.stop class = "dialog__content">
    <slot></slot>
</div>

</div>
</template>

<style scoped>
.dialog{
    top:0;
    bottom: 0;
    right: 0;
    left: 0;
    background:rgba(0,0,0 0.5);
    position: fixed;
    display: flex;
    border: 1px solid rgb(47, 209, 209);
}
.dialog__content{
    margin: auto;
    background:none;
    border-radius: 12px;
    min-height: 50px;
    max-height: 300px;
    padding: 20px;
    border: 1px solid rgb(47, 209, 209);

}
</style>

<script>
export default{
    name:'my-dialog',
    props:{
        show:{
            type:Boolean,
            default: false
        }
    },
    methods:{hideDialog(){
        this.$emit('update:show',false)
    }}
}
</script>