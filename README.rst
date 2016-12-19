record-ip-to-dnspod
===================

Record machine's ip to DNSpod via `DNSPod API`_.



示例配置文件::


    [record-ip]
    log-path = record-ip.log
    ; 文档:https://support.dnspod.cn/Kb/showarticle/tsid/227
    token = 1234,your-token-str
    ; 联系邮箱， 用于生成User-Agent
    email = me@codeif.com
    ; 域名， 例如 codeif.com
    domain = codeif.com
    ; # 不包含域名，比如test.codeif.com, 则填写test
    sub-domain = test
    ; interface = eth0
    ; exclude-ips = 127.0.0.1,172.16.0.1

- 必填配置项

log_path        日志路径
token           DNSPod API的Token_, 例如：13490,6b5976c68aba5b14a0558b77c17c3932&format=json
email
domain
sub_domain


- 可选配置项

interface       只记录指定的网卡，例如: eth0
excluet-ips     不记录下面的ip， 比如'127.0.0.1,172.16.0.1'


.. _Token: https://support.dnspod.cn/Kb/showarticle/tsid/227
.. _DNSPod API: http://www.dnspod.cn/docs/index.html
