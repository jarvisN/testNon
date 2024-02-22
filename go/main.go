package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// GET: ดึงข้อมูลผู้ใช้ด้วย ID
	r.GET("/user/:id", func(c *gin.Context) {
		id := c.Param("id")
		// จำลองการดึงข้อมูลผู้ใช้จาก ID
		c.JSON(http.StatusOK, gin.H{"userID": id, "name": "John Doe"})
	})
	// GET แบบใช้ query()
	r.GET("/search", func(c *gin.Context) {
		// ใช้ c.Query() เพื่อเข้าถึง query parameter
		query := c.Query("query") // คืนค่าเป็น string ถ้า "query" ไม่มีจะคืนค่าเป็น ""
		// หรือใช้ c.DefaultQuery() เพื่อระบุค่า default หากไม่พบ parameter
		page := c.DefaultQuery("page", "1") // ถ้า "page" ไม่มี, จะใช้ค่า "1"
		fmt.Println("test")
		// สร้าง response ที่มีข้อมูล query และ page
		c.JSON(http.StatusOK, gin.H{
			"query": query,
			"page":  page,
		})
	})

	// POST: สร้างผู้ใช้ใหม่
	r.POST("/user", func(c *gin.Context) {
		var newUser struct {
			Name  string `json:"name"`
			Email string `json:"email"`
		}
		if err := c.BindJSON(&newUser); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		// จำลองการบันทึกผู้ใช้ใหม่
		c.JSON(http.StatusCreated, gin.H{"name": newUser.Name, "email": newUser.Email})
	})

	// PUT: อัปเดตข้อมูลผู้ใช้
	r.PUT("/user/:id", func(c *gin.Context) {
		id := c.Param("id")
		var updateUser struct {
			Name  string `json:"name"`
			Email string `json:"email"`
		}
		if err := c.BindJSON(&updateUser); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		// จำลองการอัปเดตข้อมูลผู้ใช้
		c.JSON(http.StatusOK, gin.H{"userID": id, "name": updateUser.Name, "email": updateUser.Email})
	})

	// DELETE: ลบผู้ใช้
	r.DELETE("/user/:id", func(c *gin.Context) {
		id := c.Param("id")
		// จำลองการลบผู้ใช้
		c.JSON(http.StatusOK, gin.H{"userID": id, "deleted": true})
	})

	r.Run() // listen and serve on 0.0.0.0:8080
}
