<template>
    <div class="core-wrap">
        <div class="core">
            <div class="main">
                <div class="machine">
                </div>
                <div class="progress">
                    <div class="wrap">
                        <div class="inner active"></div>
                    </div>
                    <div class="wrap">
                        <div class="inner active"></div>
                    </div>
                    <div class="wrap">
                        <div class="inner"></div>
                    </div>
                </div>
                <div class="ore">
                    <s></s>
                    <span>{{ mayNum }}</span>
                </div>
                <i class="ware icon iconfont icon-money"></i>
            </div>
            <div class="bt clearFix">
                <router-link to="/mining/promote" tag="button" type="button" class="mui-btn">
                    <i class="ware icon iconfont icon-navigation-o"></i>
                    <span>提升算力</span>
                    <span class="mui-badge num">{{ miningInfo.force }}</span>
                </router-link>
                <router-link to="/mining/invitation" tag="button" type="button" class="mui-btn">
                    <i class="ware icon iconfont icon-group-o"></i>
                    <span>邀请好友</span>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => {
        return {
            miningInfo: {},
            mayNum : 0  // 当前可领取的矿石
        }
    },
    created: function() {
        this.getMiningInfo()
        this.getMay()
    },
    methods: {
        // 获取当前登录用户的矿机信息
        async getMiningInfo() {
            const { data: { data } } = await this.$axios.get('mining/get/login/')
            this.miningInfo = data
            console.log(this.miningInfo.add_time)
        },
        // 获取当前可领取的矿石
        async getMay(){
            const {data: { data: { may_num } } } = await this.$axios.get('mining/get/may/')
            this.mayNum = may_num
        }
    }
    
}
</script>

<style lang="less" scoped>
.core-wrap{
    padding: 108rem/100 25rem/100 30rem/100 25rem/100;
    .core{
        width: 100%;
        overflow: hidden;
        border-radius: 15rem/100;
        box-shadow: 0 4px 8px #ddd;

        .main{
            position: relative;
            width: 100%;
            height: 450rem/100;
            background: gradient(linear,left top,right bottom,from(#45bffd), to(#3a6af2));
            background: -webkit-gradient(linear,left top,right bottom,from(#45bffd), to(#3a6af2));

            .machine{
                position: absolute;
                top: 53%;
                margin-top: -90rem/100;
                left: 20rem/100;
                width: 178rem/100;
                height: 178rem/100;
                background: url(../../image/machine.png) no-repeat center;
                background-size: 178rem/100 178rem/100;
                animation: machine-rotate 2.5s linear infinite;
                -webkit-animation: machine-rotate 2.5s linear infinite;
            }

            .progress{
                position: absolute;
                top: 53%;
                transform: translateY(-50%);
                left: 220rem/100;
                .wrap{
                    margin-bottom: 40rem/100;
                    width: 450rem/100;
                    height: 15rem/100;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    overflow: hidden;

                    .inner{
                        width: 0;
                        height: 100%;
                        background: #fff;

                        &.active{
                            width: 100%;
                            transition: width 1000000000s linear;
                        }
                    }
                    
                    &:nth-child(3){
                        margin-bottom: 0;
                    }        
                }
            }

            .ore{
                position: absolute;
                top: 25rem/100;
                right: 25rem/100;
                padding: 10rem/100;
                width: 120rem/100;
                height: 120rem/100;
                text-align: center;
                background: #51adf9;
                border-radius: 50%;
                animation: ore-updown .8s linear infinite alternate;


                s{  
                    display: inline-block;
                    position: absolute;
                    top: 10rem/100;
                    left: 50%;
                    transform: translateX(-50%);
                    -webkit-transform: translateX(-50%);
                    width: 48rem/100;
                    height: 48rem/100;
                    background: url(../../image/stars-white.png) no-repeat center;
                    background-size: 45rem/100 45rem/100;
                }

                span{
                    display: inline-block;
                    position: absolute;
                    bottom: 20rem/100;
                    left: 50%;
                    transform: translateX(-50%);
                    -webkit-transform: translateX(-50%);
                    color: #fff;
                    font-size: 12rem/100;
                }
            }

            .ware{
                position: absolute;
                bottom: 30rem/100;
                left: 50%;
                transform: translateX(-50%);
                -webkit-transform: translateX(-50%);
                color: #fff;
                font-size: 85rem/100;
            }

        }

        .bt{
            padding: 17rem/100 20rem/100;
            width: 100%;
            font-size: 28rem/100;
            background: #fff;
            
            button{
                float: right;
                width: 300rem/100;

                &:first-child{
                float: left;

                .num{
                    color: #fff;
                    background: #3a6af2;
                }
                }  
            }

        }
    }
}

@keyframes machine-rotate {
    from{
        transform: rotate(0deg);
    }
    to{
        transform: rotate(360deg);
    }
} 

@keyframes ore-updown{
    from{
        transform: translateY(8rem/100);
    }
    to{
        transform: translateY(-4rem/100);
    }
}
</style>
