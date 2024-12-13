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

- [AI Regulation](https://medium.com/odds-team/ai-regulation-cc8f22b7579b?source=rss-4f2a1494b85e------2)
- [ODT ไป Web Summit 2024](https://medium.com/odds-team/odt-%E0%B9%84%E0%B8%9B-web-summit-2024-3d8729aca113?source=rss-4f2a1494b85e------2)
- [Wardley Map](https://medium.com/odds-team/wardley-map-92e1e2c92775?source=rss-4f2a1494b85e------2)
- [Sign in with Google บน Rails](https://medium.com/odds-team/sign-in-with-google-%E0%B8%9A%E0%B8%99-rails-d90b490c5678?source=rss-4f2a1494b85e------2)
- [Product Ownership](https://medium.com/odds-team/product-ownership-9af98752f3a9?source=rss-4f2a1494b85e------2)
- [เมื่อ User requirement ไม่ได้มีความสำคัญ](https://medium.com/odds-team/%E0%B9%80%E0%B8%A1%E0%B8%B7%E0%B9%88%E0%B8%AD-user-requirement-%E0%B9%84%E0%B8%A1%E0%B9%88%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%A1%E0%B8%B5%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%AA%E0%B8%B3%E0%B8%84%E0%B8%B1%E0%B8%8D-4d068fb73e87?source=rss-4f2a1494b85e------2)
- [เข้าใจกันอย่างโรแมนติก และจากกันไปอย่างคลาสสิก](https://medium.com/odds-team/%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B9%83%E0%B8%88%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%82%E0%B8%A3%E0%B9%81%E0%B8%A1%E0%B8%99%E0%B8%95%E0%B8%B4%E0%B8%81-%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%88%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%84%E0%B8%9B%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%AA%E0%B8%AA%E0%B8%B4%E0%B8%81-de24195115e9?source=rss-4f2a1494b85e------2)
- [Values, Logics และ Facts](https://medium.com/odds-team/values-logics-%E0%B9%81%E0%B8%A5%E0%B8%B0-facts-117c2d675f54?source=rss-4f2a1494b85e------2)
- [แค่เพียงลองโอบกอดเงาของเราเอง](https://medium.com/odds-team/%E0%B9%81%E0%B8%84%E0%B9%88%E0%B9%80%E0%B8%9E%E0%B8%B5%E0%B8%A2%E0%B8%87%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%82%E0%B8%AD%E0%B8%9A%E0%B8%81%E0%B8%AD%E0%B8%94%E0%B9%80%E0%B8%87%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%A3%E0%B8%B2%E0%B9%80%E0%B8%AD%E0%B8%87-a48835e47406?source=rss-4f2a1494b85e------2)
- [ความเชื่อใจ (Trust)](https://medium.com/odds-team/%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B9%83%E0%B8%88-trust-db5ca6bc915c?source=rss-4f2a1494b85e------2)

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
