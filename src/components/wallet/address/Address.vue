<template>
    <div class="wallet-address-wrap">
        <div class="mask"></div>
        <div class="address-box">
            <TitleBar v-bind:title-obj="titleObj"></TitleBar>
            <div class="box-wrap">
                <div class="box">
                    <h3>我的钱包地址</h3>
                    <div class="erweima"></div>
                    <p>0x54d3a7c8E4177Ad8BD265012E0bd015ABC7ceD4F</p>
                    <div class="line">
                        <s></s>
                        <s></s>
                    </div>
                    <button type="button" class="mui-btn">
                        复制钱包地址
                    </button>
                </div>
            </div>      
        </div>
    </div>
</template>

<script>
import TitleBar from '../../Title-Bar.vue'

export default {
    data () {
        return {
            titleObj: {
                title: '钱包地址',
                bold: false,
                back: true,
                ditails: false
            }
        }
    },
    components: {
        TitleBar
    }
}
</script>

<style lang="less" scoped>
    .mask{
        position: fixed;
        z-index: 100;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: #f5f5f5;
    }

    .address-box{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 101;

        .box-wrap{
            margin-top: 88rem/100;
            padding: 20rem/100 25rem/100;
            width: 100%;

            .box{
                padding: 35rem/100 0;
                width: 100%;
                text-align: center;
                border-radius: 10px;
                background: #fff;
                box-shadow: 0px 4px 8px #ddd;

                h3{
                    margin: 0;
                    width: 100%;
                    text-align: center;
                    font-size: 34rem/100;
                    font-weight: normal;
                    color: #333;
                }

                .erweima{
                    display: inline-block;
                    margin: 20rem/100 0;
                    width: 200rem/100;
                    height: 200rem/100;
                    background: url(../../../image/erweima.png) no-repeat center;
                    background-size: 200rem/100 200rem/100;
                }

                p{
                    margin: 10rem/100 auto;
                    width: 400rem/100;
                    word-wrap: break-word;
                    word-break: break-all;
                    overflow: hidden;
                }

                .line{
                    position: relative;
                    width: 100%;
                    border-top: 1px dashed #3a6af2;

                    s{  
                        position: absolute;     
                        display: block;
                        width: 45rem/100;
                        height: 45rem/100;
                        border-radius: 50%;
                        background: #f5f5f5;

                        &:first-child{
                            left: 0;
                            top: 0;
                            transform: translateX(-50%) translateY(-50%);
                        }

                        &:last-child{
                            right: 0;
                            top: 0;
                            transform: translateX(50%) translateY(-50%);
                        }
                    }
                }

                button{
                    margin-top: 30rem/100;
                    padding: 15rem/100 80rem/100;
                    width: 550rem/100;
                    height: 70rem/100;
                    color: #fff;
                    border-radius: 5px;
                    background: #3a6af2;
                }

            }
        }
    }
    
</style>