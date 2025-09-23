# Hello folks!

```go
package main

import "fmt"

type Person struct {
	Name     string
	Pronouns []string
}

func (p *Person) Greet() string {
	return fmt.Sprintf("Hello! I'm %s.", p.Name)
}

func main() {
	me := &Person{
		Name:     "chonla",
		Pronouns: []string{"he", "him", "his"},
	}
	fmt.Println(me.Greet())
}
```

## Blogs

- [จัดระเบียบ Page Object Model ด้วย Mixins และ Decorators](https://medium.com/odds-team/%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9A%E0%B8%B5%E0%B8%A2%E0%B8%9A-page-object-model-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-mixins-%E0%B9%81%E0%B8%A5%E0%B8%B0-decorators-0dc2b3568f3d?source=rss-4f2a1494b85e------2)
- [mise โคตรเครื่องมือสำหรับ developer](https://medium.com/odds-team/mise-%E0%B9%82%E0%B8%84%E0%B8%95%E0%B8%A3%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-developer-3487e283785c?source=rss-4f2a1494b85e------2)
- [ใช้ localhost ให้เท่ขึ้นแบบคูณสาม](https://medium.com/odds-team/%E0%B9%83%E0%B8%8A%E0%B9%89-localhost-%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%80%E0%B8%97%E0%B9%88%E0%B8%82%E0%B8%B6%E0%B9%89%E0%B8%99%E0%B9%81%E0%B8%9A%E0%B8%9A%E0%B8%84%E0%B8%B9%E0%B8%93%E0%B8%AA%E0%B8%B2%E0%B8%A1-eeb581965c07?source=rss-4f2a1494b85e------2)
- [ซ่อนบาร์ของ Browser](https://medium.com/odds-team/%E0%B8%8B%E0%B9%88%E0%B8%AD%E0%B8%99%E0%B8%9A%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%82%E0%B8%AD%E0%B8%87-browser-2d07a5478df3?source=rss-4f2a1494b85e------2)
- [Agile Transformation — The PST](https://medium.com/odds-team/agile-transformation-the-pst-589a07150b7f?source=rss-4f2a1494b85e------2)
- [Agile Transformation — Supply &amp; Demand](https://medium.com/odds-team/agile-transformation-supply-demand-84e21ed636b2?source=rss-4f2a1494b85e------2)
- [ทำให้ Dev Environment เหมือนกันด้วย devbox](https://medium.com/odds-team/%E0%B8%97%E0%B8%B3%E0%B9%83%E0%B8%AB%E0%B9%89-dev-environment-%E0%B9%80%E0%B8%AB%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-devbox-330741fe34c0?source=rss-4f2a1494b85e------2)
- [ทดสอบของที่ต้องแตะ database บน NestJS ด้วย in-memory database](https://medium.com/odds-team/%E0%B8%97%E0%B8%94%E0%B8%AA%E0%B8%AD%E0%B8%9A%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B9%81%E0%B8%95%E0%B8%B0-database-%E0%B8%9A%E0%B8%99-nestjs-%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-in-memory-database-54925db7f6ba?source=rss-4f2a1494b85e------2)
- [AI Regulation](https://medium.com/odds-team/ai-regulation-cc8f22b7579b?source=rss-4f2a1494b85e------2)
- [ODT ไป Web Summit 2024](https://medium.com/odds-team/odt-%E0%B9%84%E0%B8%9B-web-summit-2024-3d8729aca113?source=rss-4f2a1494b85e------2)

## Pinned repositories

I have created many public repositories. These are some of them.

| Name | Description |
| --- | --- |
| [cotton](https://github.com/chonla/cotton) | Markdown Test Specification Runner |
| [thai-address](https://github.com/chonla/thai-address) | Yet Another Thai Address Package |
| [thai-address-builder](https://github.com/chonla/thai-address-builder) | A script to build thai address data for thai address npm package. |
| [cellwalker](https://github.com/chonla/cellwalker) | Excel Cell Name Traversal for Go |
| [thai-financial-instiutions-holiday](https://github.com/chonla/thai-financial-instiutions-holiday) | Up-to-date Thai Financial Institutions Holiday |
| [csv2img](https://github.com/chonla/csv2img) | Create CSV Table Image |

[See more](https://github.com/chonla?tab=repositories).

## Holopin badges

[![An image of @chonla's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/chonla)](https://holopin.io/@chonla)

## Codewars badge

[![An image of chonla's codewars badge.](https://www.codewars.com/users/chonla/badges/large)](https://www.codewars.com/users/chonla)
