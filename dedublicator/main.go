package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"image"
	"image/jpeg"
	"log"
	"os"
	"path/filepath"
	"strings"
)

// calculateMD5Hash calculates the MD5 hash of an image file
func calculateMD5Hash(filePath string) (string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return "", err
	}
	defer file.Close()

	hash := md5.New()
	_, err = image/jpeg.Decode(file)
	if err != nil {
		// If not a JPEG, try to read as a stream to hash the bytes
		_, err = hash.Write(ReadFileBytes(filePath))
		if err != nil {
			return "", err
		}
	} else {
		// Reopen the file since we consumed it with Decode
		file, err = os.Open(filePath)
		if err != nil {
			return "", err
		}
		defer file.Close()
		_, err = hash.Write(ReadFileBytes(filePath))
		if err != nil {
			return "", err
		}
	}

	return hex.EncodeToString(hash.Sum(nil)), nil
}

// ReadFileBytes reads the content of a file into a byte array
func ReadFileBytes(filePath string) []byte {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	stats, err := file.Stat()
	if err != nil {
		log.Fatal(err)
	}

	var size = stats.Size()
	bytes := make([]byte, size)

 buf := make([]byte, 1024)
	for {
		n, err := file.Read(buf)
		if err != nil {
			break
		}
		bytes = append(bytes, buf[:n]...)
	}

	return bytes
}

// findAndRemoveDuplicates searches for duplicate images in a directory and removes them
func findAndRemoveDuplicates(directory string) {
	// Map to store hashes as keys and file paths as values
	hashToFilePath := make(map[string][]string)

	// Walk through the directory
	err := filepath.WalkDir(directory, func(path string, dirEntry os.DirEntry, err error) error {
		if !dirEntry.IsRegular() || !strings.HasSuffix(dirEntry.Name(), ".jpg") && !strings.HasSuffix(dirEntry.Name(), ".jpeg") {
			return nil // Ignore non-regular files and non-image files
		}

		hash, err := calculateMD5Hash(path)
		if err != nil {
			log.Printf("Error calculating hash for %s: %v\n", path, err)
			return nil
		}

		hashToFilePath[hash] = append(hashToFilePath[hash], path)
		return nil
	})

	if err != nil {
		log.Fatal(err)
	}

	// Find and remove duplicates
	for hash, paths := range hashToFilePath {
		if len(paths) < 2 {
			continue // Not a duplicate
		}

		fmt.Printf("Found duplicates with hash %s:\n", hash)
		for i, path := range paths {
			if i == 0 {
				fmt.Printf("  Keeping: %s\n", path)
			} else {
				fmt.Printf("  Removing: %s\n", path)
				err := os.Remove(path)
				if err != nil {
					log.Printf("Failed to remove %s: %v\n", path, err)
				}
			}
		}
	}
}

func main() {
	directory := "../photos" 
	fmt.Printf("Scanning for duplicates in directory: %s\n", directory)
	findAndRemoveDuplicates(directory)
	fmt.Println("Done.")
}
