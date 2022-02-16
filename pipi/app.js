//app.js
App({
  onLaunch: function () {
    //调用API从本地缓存中获取数据
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    //获取登录用户唯一id--openId
    var _this = this
   
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
         
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo
              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }else {
          // 没有授权，重定向到 loading 启动页
          wx.navigateTo({
            url: '/pages/loading/loading'
          })
        }
        }
        })

    wx.login({
      success: function (res) {
        if (res.code) {
          //发起网络请求
          wx.request({
            url: 'https://api.weixin.qq.com/sns/jscode2session',
            data: {
              js_code: res.code,
              secret: 'e7a29bcff6cdca08f6e3c58a272febd9',
              appid: 'wxa1fc22496a14c3d9',
              grant_type: 'authorization_code'
            },
            success: res => {
              _this.globalData.openid = res.data.openid
              console.log("openid=" + _this.globalData.openid)
            }
          })
        } else {
          console.log('获取用户登录态失败！' + res.errMsg)
        }
      }
    })

       
    /**
     * 得到商家信息
     */
    wx.request({
      url: _this.getHeader() + '/shop/getInfo',
      data: {
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success: function (res) {
        if (res.data.status == 200) {
          _this.globalData.business.name = res.data.data.name
          _this.globalData.business.address = res.data.data.address
          _this.globalData.business.mobile = res.data.data.phone
          _this.globalData.business.time = res.data.data.time
        } else {
          _this.showToast(res.data.msg)
        }
        console.log("请求的商家信息", _this.globalData.business)
      },
      fail() {
        _this.showToast()
      }
    })
  },
  
  onLoad: function () {

  },

  globalData: {
    userInfo: null,
    location: "",
    city: '',
    address: '',
    buycar_num: 0,
    totalMoney: 0,
    totalSecond: 899,
    //请求的ip地址和端口号，请求协议
    protocol: "http://",
    // host: "47.106.168.136",
    // port: "8888",
    host: "127.0.0.1",
    port: 8000,
    openid: '',//用户唯一标志ids
    /**
     * 商户信息
     */
    business: {
      name: '',
      address: '',
      time: '',
      mobile: '',
      avatarUrl: '../../img/qishou.png'
    },
  },
  /**
  * 封装请求头
  */
  getHeader() {
    var protocol = this.globalData.protocol
    var host = this.globalData.host
    var port = this.globalData.port
    var header = protocol + host + ':' + port
    return header;
  },
  showToast(title, duration, icon) {
    wx.showToast({
      title: title ? title : '网络繁忙，请扫后重试！',
      duration: duration || 1000,
      icon: icon || 'none'
    })
  }



})
